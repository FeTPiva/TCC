# coding: utf-8
import nltk
import csv

#lembrar de alterar qnd for rodar no main geral
import baseEmocao as baseEmocao


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

def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavras_unicas_treinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


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

#Aqui vai a frase processada pelo felipe
fraseteste = 'Meu dia não foi bom, gostaria de estar sozinho no meu quarto'
testestemming = []
stemmer = nltk.stem.RSLPStemmer()

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





