import mysql.connector
import Pre_processamento.Corretor as Corretor
# Conexao com Banco de Dados

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


def obterLinhaTexto(idPessoa):  #Fernanda
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

#retorno geral de textos limitando por ntextos, por cada pessoa
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