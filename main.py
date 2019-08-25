#fazer os import
import nltk
import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import csv
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao


input_n_textos = 2

pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'
superString = []
primeiroParse = {}
dictemocao = {'alegria':1,'raiva':2,'tristeza':3,'desgosto':4,'medo':5,'surpresa':6,'neutro':7}

#ok
def criaLista(val1, val2, val3, val4):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
    lista.insert(3, val4)
    return lista

#ok
def criaListaCsv(val1, val2, val3, val4, val5, val6, val7, val8, val9):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
    lista.insert(3, val4)
    lista.insert(4, val5)
    lista.insert(5,val6)
    lista.insert(6, val7)
    lista.insert(7, val8)
    lista.insert(8, val9)
    return lista

#ok
def retornaContagem(idPessoa, nTextos, txtPronomes, txtAbsolutas, txtTristes):
    pessoa = idPessoa+1
    mylist = ConnectionDB.retornaTextosPorPessoa(pessoa, nTextos)
    primeiroParse = mylist[idPessoa]
    #print(primeiroParse)
    segundoParse = primeiroParse["texto"]
    #print(segundoParse)

    textoTratado1 = contagem.contandoCoisas(segundoParse,pronome)
    textoTratado2 = contagem.contandoCoisas(segundoParse,absoluta)
    textoTratado3 = contagem.contandoCoisas(segundoParse,triste)

    
    idDepre = primeiroParse["isDepressivo"]
    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3, idDepre)
    print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista



c = ConnectionDB.totalPessoas()
x=0

while x < c:
    
    contagem_palavras = retornaContagem(x, input_n_textos, pronome, absoluta, triste)

    #sentimentos = mineracaoemocao.retornaProbs(input_n_textos, x+1)
    #probs_csv = criaListaCsv(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos[0], sentimentos[1], sentimentos[2], sentimentos[3], sentimentos[4], sentimentos[5])



    #print(lista)
    with open('csv/contagem.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(contagem_palavras)
    
    x+=1

