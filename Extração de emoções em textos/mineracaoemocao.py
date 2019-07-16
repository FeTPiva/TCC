# coding: utf-8
import nltk

basetreinamento = []
for line in open('base treinamento.txt', 'r'):
    basetreinamento.append(line.strip())
 
baseteste = []
for line in open('base teste.txt', 'r'):
    baseteste.append(line.strip())

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
    for palavras in palavrasunicastreinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


frasescomstemmingtreinamento = aplicastemmer(basetreinamento)
frasescomstemmingteste = aplicastemmer(baseteste)

palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)
palavrasteste = buscapalavras(frasescomstemmingteste)

frequenciatreinamento = buscafrequencia(palavrastreinamento)
frequenciateste = buscafrequencia(palavrasteste)

palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = buscapalavrasunicas(frequenciateste)

basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento)
basecompletateste = nltk.classify.apply_features(extratorpalavras, frasescomstemmingteste)

# constroi a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)

erros = []
for (frase, classe) in basecompletateste:
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado, frase))

from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []
for (frase, classe) in basecompletateste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)

matriz = ConfusionMatrix(esperado, previsto)

fraseteste = 'Meu dia não foi bom, gostaria de estar sozinho no meu quarto'
testestemming = []
stemmer = nltk.stem.RSLPStemmer()

for (palavrastreinamento) in fraseteste.split():
    comstem = [p for p in palavrastreinamento.split()]
    testestemming.append(str(stemmer.stem(comstem[0])))

novo = extratorpalavras(testestemming)

distribuicao = classificador.prob_classify(novo)
for classe in distribuicao.samples():
    print("%s: %f" % (classe, distribuicao.prob(classe)))