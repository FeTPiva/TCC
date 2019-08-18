#fazer os import
import nltk
import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import csv
import ExtracaodeEmocoesemTextos.mineracaoemocao as mineracaoemocao

pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'
superString = []
primeiroParse = {}
dictemocao = {'alegria':1,'raiva':2,'tristeza':3,'desgosto':4,'medo':5,'surpresa':6,'neutro':7}

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
    #print(primeiroParse)
    segundoParse = primeiroParse["texto"]
    print(segundoParse)

    textoTratado1 = contagem.contandoCoisas(segundoParse,pronome)
    textoTratado2 = contagem.contandoCoisas(segundoParse,absoluta)
    textoTratado3 = contagem.contandoCoisas(segundoParse,triste)

    
    idDepre = primeiroParse["isDepressivo"]
    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3, idDepre)
    #print(lista)
    with open('csv/contagem.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(lista)

    
    x+=1

linhasTabela = ConnectionDB.totalTextos()
i=1
while i <= linhasTabela:
    mylist = ConnectionDB.obterLinhaFrase(i)
    primeiroParse = mylist[0]
    segundoParse = primeiroParse["texto"]
    fraseteste = segundoParse
    print(fraseteste)
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()

    for (palavrastreinamento) in fraseteste.split():
        comstem = [p for p in palavrastreinamento.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))

    novo = mineracaoemocao.extratorpalavras(testestemming)
    distribuicao = mineracaoemocao.classificador.prob_classify(novo)
    
    #Vetor para saida
    vetorsaida = []
    for classe in distribuicao.samples():
        vetorsaida.append(dictemocao.get(classe))
        vetorsaida.append(distribuicao.prob(classe))

    #Importar resultado para csv
    with open('saida.csv', 'a', newline = '') as csvfile:   
        writer = csv.writer(csvfile) 
        writer.writerow(vetorsaida)
    
    print(vetorsaida)
    i+=1
