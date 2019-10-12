import nltk
from nltk.stem import RSLPStemmer
#import Pre_processamento.ConnectionDB as ConnectionDB

import mysql.connector


mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="senha666",
database="depressao"
)


def retornaTextosSQLPOL():  
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(palavra SEPARATOR ' ') FROM tbl_polaridade ") 
	myresult = mycursor.fetchall()
    
	return myresult[0]

def retornaVetorSQLPOL():
    data = []	
    mycursor = mydb.cursor()
    mycursor.execute(" SELECT palavra, polaridade FROM tbl_polaridade; ") 
    myresult = mycursor.fetchall()
    for x in myresult:
        jsonData = {
            "palavra": x[0],
            "pol": x[1]
        }
        data.append(jsonData)
    
    return data

def insertSQLPOL(txt,pol):
    mycursor = mydb.cursor()
    mycursor.execute(" insert into newpol (palavra, polaridade) values (%s ,%i); "%(txt,pol))
     

def toltalRegistrosPOL():
    data = []	
    mycursor = mydb.cursor()
    mycursor.execute(" SELECT COUNT(idpolaridade) FROM tbl_polaridade") 
    data = mycursor.fetchone()

    return data[0]

def obterLinhaTextoPOL(idPessoa):  #Fernanda - versao antiga
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(texto SEPARATOR ', '), isDepressivo FROM tbl_polaridade WHERE idPessoa= " + str(idPessoa)) 
	myresult = mycursor.fetchall()
	
	return myresult[0]


def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase


def polarizandoCoisas(texto):

    p = 0
    
    texto = Tokenize(texto)

    #texto = Stemming(texto)

    i = 0
    t = toltalRegistrosPOL()
    mylist = retornaVetorSQLPOL()    

    while i < t:
        primeiroParse = mylist[i]                
        segundoParse = primeiroParse["palavra"]
        pol = primeiroParse["pol"]
        primeiroParse.clear()
        for word in texto :
            if word in segundoParse :
                p = p+pol
        i+=1
  
    return p
    
def polarizando(idPessoa):

    segundoParse = ""
    
    pessoa = idPessoa+1
    

    segundoParse = obterLinhaTextoPOL(pessoa)
    #with open(textoAnalisado, 'r') as document_text:
    #    texto = document_text.read()
    #primeiroParse = mylist[0]
      #  print("primeiro parse", primeiroParse)
      
    #segundoParse = primeiroParse["texto"]
    #isDepre = primeiroParse["isDepressivo"]
    #primeiroParse.clear()
       
    polarization = polarizandoCoisas(segundoParse)

    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(polarization)
    #print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista


def criaLista(*args):
    lista = []
    i=0
    c = len(args)

    while i < c:
               
        lista.insert(i, args[i])
        i+=1
      
    return lista


#a = retornaTextosSQL()
#lista = ['a','b']
#a = retornaVetorSQL()
#a = toltalRegistros()
#a = polarizandoCoisas("temor ")


#print(a)