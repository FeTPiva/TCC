import nltk
from nltk.stem import RSLPStemmer

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="senha666",
database="depressao"
)


def retornaTextosSQL():  
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(palavra SEPARATOR ' ') FROM tbl_polaridade ") 
	myresult = mycursor.fetchall()
    
	return myresult[0]

def retornaVetorSQL():
    data = []	
    mycursor = mydb.cursor()
    mycursor.execute(" SELECT palavra, polaridade FROM tbl_polaridade ; ") 
    myresult = mycursor.fetchall()
    for x in myresult:
        jsonData = {
            "palavra": x[0],
            "pol": x[1]
        }
        data.append(jsonData)
    
    return data

def toltalRegistros():
    data = []	
    mycursor = mydb.cursor()
    mycursor.execute(" SELECT COUNT(idpolaridade) FROM tbl_polaridade") 
    data = mycursor.fetchone()

    return data[0]


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
       
    print(texto)
    i = 0
    t = toltalRegistros()
    mylist = retornaVetorSQL()    

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


def criaLista(*args):
    lista = []
    i=0
    c = len(args)

    while i < c:
               
        lista.insert(i, args[i])
        i+=1
      
    return lista


#a = retornaTextosSQL()
lista = ['a','b']
#a = retornaVetorSQL()
#a = toltalRegistros()
a = polarizandoCoisas("soberba temor revoltado")

print(a)