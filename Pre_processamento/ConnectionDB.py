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
	mycursor.execute("SELECT MAX(idPessoa) FROM textodepressao")
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
def retornaTextosPorPessoaTokenContagem(idPessoa, nToken): 
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(SUBSTRING_INDEX(texto , " ", ?) SEPARATOR ', '), isDepressivo FROM textodepressao WHERE idPessoa= ? ;",(nToken,idPessoa)) 
	
	myresult = mycursor.fetchall()

	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
	
		#pensar aki... vou acabar pegando tipo por ex 10 palavras texto, mas n é o q eu quero pro meu(contagem)	
		#frase = Tokenize(x_correto)
		#size = len(frase)		
		#fraseFiltrada = []
		#i=0
		#while i < nToken:
		#	fraseFiltrada.append(frase[i])
		#	i+=1

		jsonData = {
			"texto": x_correto,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data


#retorno geral de textos limitando por palavras, por cada pessoa - emocoes
def retornaTextosPorNmrPalavrasEmocao(idPessoa, nToken):
		
	mycursor = mydb.cursor()
	mycursor.execute("SELECT SUBSTRING_INDEX(texto," ",%s), isDepressivo FROM textodepressao WHERE idPessoa = %s ;"%(nToken,idPessoa)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])		
		jsonData = {
			"texto": x_correto,
			"isDepressivo": x[1]
		}
		data.append(jsonData)
	return data

#retorno textos por pessoa sem filtro - pt pra emocoes
def retornaNTextosGeral(idPessoa):
		
	mycursor = mydb.cursor()
	mycursor.execute("SELECT texto FROM textodepressao WHERE idPessoa = %s ;"%(idPessoa)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		jsonData = {
			"texto": x_correto
		}
		data.append(jsonData)
	return data

#nmr de textos de cada pessoa
def nmrTextosPorPessoa(idPessoa):
	mycursor = mydb.cursor()
	mycursor.execute("SELECT COUNT(idPessoa) FROM textodepressao WHERE idPessoa = %s ;"%(idPessoa))
	myresult = mycursor.fetchone()
	return myresult[0]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PARA X TESTESSS:

def obterLinhaTextoxTeste(idPessoa): 
	data = []	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT GROUP_CONCAT(texto SEPARATOR ', ') FROM tbl_xteste WHERE idPessoa= " + str(idPessoa)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		
	return x_correto


def retornaNTextosGeral_xTeste(idPessoa):
		
	mycursor = mydb.cursor()
	mycursor.execute("SELECT texto FROM tbl_xteste WHERE idPessoa = %s ;"%(idPessoa)) 
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		
	return x_correto