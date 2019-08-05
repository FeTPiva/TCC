import contagem
import re
import string
import dictemp
import operator
import csv

#https://stackoverflow.com/questions/28277150/write-a-list-in-a-python-csv-file-one-new-row-per-list

#textoAnalisado = 'teste1.txt'
pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'
superString = []
primeiroParse = {}

def retornaTamanho():
    return 3

def criaLista(val1, val2, val3, val4):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
    lista.insert(3, val4)
    return lista
#meuDic = dictemp.enviaFraseProcessada()
#textoAnalisado = meuDic["texto"]
#depressividade = meuDic["isDepressivo"]

#print(textoAnalisado,depressividade)
#mylist = dictemp.enviaFraseProcessada()
#a = mylist[0]
#b= mylist[1]
#txta = a["texto"]
#txtb = b["texto"]
#print(txta)
#print(txtb)
#for x in mylist:
#  print(x)
#for x in mylist:
#    superString = x["texto"]
#a = map(operator.itemgetter("Text"), mylist)
#print(a)

c = retornaTamanho()
x=0

while x < c:
    mylist = dictemp.enviaFraseProcessada()
    primeiroParse = mylist[x]
    print(primeiroParse)
    segundoParse = primeiroParse["texto"]
    print(segundoParse)

    textoTratado1 = contagem.contandoCoisas(segundoParse,pronome)
    textoTratado2 = contagem.contandoCoisas(segundoParse,absoluta)
    textoTratado3 = contagem.contandoCoisas(segundoParse,triste)
    idDepre = primeiroParse["isDepressivo"]
    print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3, idDepre)
    print(lista)
    #esse aki insere uma linha só
    with open('csv/contagem.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(lista)

    #with open('teste.csv', "r") as infile:
    #    reader = list(csv.reader(infile))
    #    reader.insert(1, lista)

    #with open('teste.csv', "w") as outfile:
    #    writer = csv.writer(outfile)
    #    for line in reader:
    #        writer.writerow(line)
    x+=1
