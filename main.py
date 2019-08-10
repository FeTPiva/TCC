#fazer os import

import Pre_processamento.ConnectionDB as ConnectionDB

import contagem_de_palavras.contagem as contagem
import csv

pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'
superString = []
primeiroParse = {}

def criaLista(val1, val2, val3, val4):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
    lista.insert(3, val4)
    return lista


c = ConnectionDB.totalPessoas()
x=0


while x < c:
    mylist = ConnectionDB.obterLinhaTexto(x+1)
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
    with open('csv/contagem.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(lista)

    
    x+=1
