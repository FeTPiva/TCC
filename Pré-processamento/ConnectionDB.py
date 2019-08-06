import mysql.connector
import Corretor 
# Conexao com Banco de Dados
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="root",
database="depressao"
)
	
def totalPessoas():		#Fernanda
	mycursor = mydb.cursor()
	mycursor.execute("SELECT COUNT(idPessoa) FROM Pessoa");
	myresult = mycursor.fetchone()
	return myresult[0]

def obterLinhaFrase(idPessoa):  #Vinicius
	data = []
	mycursor = mydb.cursor()
	mycursor.execute("SELECT texto FROM textodepressao WHERE idPessoa = " + str(idPessoa))
	myresult = mycursor.fetchall()
	for x in myresult:
		x_correto = Corretor.correct_phrase(x[0])
		jsonData = {
			"texto": x_correto
		}
		data.append(jsonData)
	return data

def obterLinhaTexto(idPessoa):  #Fernanda
	
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
		
'''  Fernanda teste
data = []
y=1
z = totalPessoas()
print(z)
while y <= z:
	print(obterLinhaTexto(y))
	y+=1
'''


for i in total:
	print(obterLinhaFrase(1))


