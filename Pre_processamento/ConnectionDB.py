import mysql.connector
import Pre_processamento.Corretor as Corretor
# Conexao com Banco de Dados
import nltk


def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence


mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="senha666",
database="depressao"
)
data = []	

def totalTextos():
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT COUNT(idTexto) FROM textodepressao")
	myresult = mycursor.fetchone()
	return myresult[0]
	
def totalPessoas():
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT COUNT(idPessoa) FROM Pessoa")
	myresult = mycursor.fetchone()
	return myresult[0]


def obterLinhaFrase(idTexto):  #Vinicius
	data = []
	mycursor = mydb.cursor()
	mycursor.execute("SELECT texto, isDepressivo FROM textodepressao WHERE idTexto = " + str(idTexto))
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		jsonData = {
			"texto": x_correto,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data


def obterLinhaTexto(idPessoa):  #Fernanda - versao antiga
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(texto SEPARATOR ', '), isDepressivo FROM textodepressao WHERE idPessoa= " + str(idPessoa)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		jsonData = {
			"texto": x_correto,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data

#retorno geral de textos limitando por ntextos, por cada pessoa v1
def retornaNTextos(idPessoa, nTextos):
		
	mycursor = mydb.cursor()
	mycursor.execute("SELECT texto, isDepressivo FROM textodepressao WHERE idPessoa = %s LIMIT %s ;"%(idPessoa, nTextos)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		jsonData = {
			"texto": x_correto,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data

#retorna todos os textos da pessoa juntos v1
def retornaTextosPorPessoa(idPessoa, nTextos): 
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(texto SEPARATOR ', '), isDepressivo FROM textodepressao WHERE idPessoa= %s LIMIT %s ;"%(idPessoa,nTextos)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		jsonData = {
			"texto": x_correto,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data


#retorna todos os textos da pessoa juntos v2 - pegando numero de palavras
def retornaTextosPorPessoaToken(idPessoa, nTextos, nToken): 
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(texto SEPARATOR ', '), isDepressivo FROM textodepressao WHERE idPessoa= %s LIMIT %s ;"%(idPessoa,nTextos)) 
	myresult = mycursor.fetchall()

	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
	
		#pensar aki... vou acabar pegando tipo por ex 10 palavras texto, mas n é o q eu quero pro meu(contagem)	
		frase = Tokenize(x_correto)
		#size = len(frase)		
		fraseFiltrada = []
		i=0
		while i < nToken:
			fraseFiltrada.append(frase[i])
			i+=1

		jsonData = {
			"texto": fraseFiltrada,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data


#retorno geral de textos limitando por ntextos, por cada pessoa v2 - pegando nmr de palavras
def retornaNTextosToken(idPessoa, nTextos, nToken):
		
	mycursor = mydb.cursor()
	mycursor.execute("SELECT texto, isDepressivo FROM textodepressao WHERE idPessoa = %s LIMIT %s ;"%(idPessoa, nTextos)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		frase = Tokenize(x_correto)
		#size = len(frase)		
		fraseFiltrada = []
		i=0
		while i < nToken:
			fraseFiltrada.append(frase[i])
			i+=1

		jsonData = {
			"texto": fraseFiltrada,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data