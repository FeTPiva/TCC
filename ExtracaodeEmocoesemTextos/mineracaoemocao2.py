# coding: utf-8
import nltk
import csv

#lembrar de alterar qnd for rodar no main geral
import ExtracaodeEmocoesemTextos.baseEmocao as baseEmocao

#connection do felipe
import Pre_processamento.ConnectionDB as ConnectionDB


#retorno do vetor com a base de treinamento
basetreinamento = baseEmocao.retornaTreinamento()
#retorno do vetor com a base de teste
baseteste = baseEmocao.retornaTeste()


stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
stopwordsnltk.append('vou')
stopwordsnltk.append('tão')

def removestopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases

def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming

def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

#converte em dict?
def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavras_unicas_treinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


def retornaEmocoes(idPessoa, nTextos):
    
    pessoa = idPessoa+1
    mylist = ConnectionDB.retornaNTextos(pessoa, nTextos)
    
    print(pessoa)
    print(mylist)
    
    i=0
    
    while i < nTextos:
        vetor_saida = []
        primeiroParse = mylist[i]
        segundoParse = primeiroParse["texto"]
        fraseteste = segundoParse
        testestemming = []
        stemmer = nltk.stem.RSLPStemmer()

        for (palavrastreinamento) in fraseteste.split():
            comstem = [p for p in palavrastreinamento.split()]
            testestemming.append(str(stemmer.stem(comstem[0])))

        novo = extratorpalavras(testestemming)
        
        distribuicao = classificador.prob_classify(novo)
        
        #Vetor para saida
        
        for classe in distribuicao.samples():
            #vetorsaida.append(dictemocao.get(classe))
            
            vetor_saida.append(distribuicao.prob(classe))
                       
    i+=1
       
    return vetor_saida

def retornaProbabilidadeEmocoes(idPessoa, nTextos):
    alegria = 0
    raiva = 0
    tristeza = 0
    desgosto = 0
    medo = 0
    surpresa = 0
    j = 0
    #neutro =0
    #total_linhas = ConnectionDB.retornaNTextos(idPessoa, input_n_textos)
    while j <= nTextos:
        pessoa = j+1
        vetor_saida = retornaEmocoes(pessoa, nTextos)
        alegria += vetor_saida[0]
        raiva += vetor_saida[1]
        tristeza += vetor_saida[2]
        desgosto += vetor_saida[3]
        medo += vetor_saida[4]
        surpresa += vetor_saida[5]
        #neutro += vetor_saida[6]
        print(surpresa)
        j+=1
    prob_alegria = alegria / nTextos
    prob_raiva = raiva / nTextos
    prob_tristeza = tristeza / nTextos
    prob_desgosto = desgosto / nTextos
    prob_medo = medo / nTextos
    prob_surpresa = surpresa / nTextos
    probs = [prob_alegria, prob_raiva, prob_tristeza, prob_desgosto, prob_medo, prob_surpresa]
    return probs       

frases_com_stemming_treinamento = aplicastemmer(basetreinamento)
frases_com_stemming_teste = aplicastemmer(baseteste)

palavras_treinamento = buscapalavras(frases_com_stemming_treinamento)
palavras_teste = buscapalavras(frases_com_stemming_teste)

frequencia_treinamento = buscafrequencia(palavras_treinamento)
frequencia_teste = buscafrequencia(palavras_teste)

palavras_unicas_treinamento = buscapalavrasunicas(frequencia_treinamento)
palavras_unicas_teste = buscapalavrasunicas(frequencia_teste)

base_completa_treinamento = nltk.classify.apply_features(extratorpalavras, frases_com_stemming_treinamento)
base_completa_teste = nltk.classify.apply_features(extratorpalavras, frases_com_stemming_teste)

# constroi a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(base_completa_treinamento)

erros = []
#teste para ver a precisão da rede, eu acho
for (frase, classe) in base_completa_teste:
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado, frase))

from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []
for (frase, classe) in base_completa_teste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)

matriz = ConfusionMatrix(esperado, previsto)

#COMEÇA AKI
testestemming = []
stemmer = nltk.stem.RSLPStemmer()
'''
#APLICAÇÃO DO STEMMING
for (palavras_treinamento) in fraseteste.split():
    comstem = [p for p in palavras_treinamento.split()]
    testestemming.append(str(stemmer.stem(comstem[0])))

novo = extratorpalavras(testestemming)

distribuicao = classificador.prob_classify(novo)

dictemocao = {'alegria':1,'raiva':2,'tristeza':3,'desgosto':4,'medo':5,'surpresa':6,'neutro':7}

#Vetor para saida
vetorsaida = []
for classe in distribuicao.samples():
    vetorsaida.append(dictemocao.get(classe))
    vetorsaida.append(distribuicao.prob(classe))
print(vetorsaida)

#Importar resultado para csv
with open('saida.csv', 'w') as csvfile:   
    writer = csv.writer(csvfile) 
    writer.writerow(vetorsaida)



'''

