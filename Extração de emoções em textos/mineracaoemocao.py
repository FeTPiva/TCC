# coding: utf-8
import nltk

#nltk.download()

basetreinamento = []
for line in open('base treinamento.txt', 'r'):
    basetreinamento.append(line.strip())
 
baseteste = []
for line in open('base teste.txt', 'r'):
    baseteste.append(line.strip())
    

print(basetreinamento)
#print(baseteste)

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
#print(stopwordsnltk)


#Aplica o Stemming e retira as stopwords
def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming

frasescomstemmingtreinamento = aplicastemmer(basetreinamento)
frasescomstemmingteste = aplicastemmer(baseteste)
print(frasescomstemmingtreinamento)


#busca as palavras separadas com stemmer
def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras

palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)
palavrasteste = buscapalavras(frasescomstemmingteste)
#print(palavras)


#mostra freq das palavras com stemmer
def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequenciatreinamento = buscafrequencia(palavrastreinamento)
frequenciateste = buscafrequencia(palavrasteste)
#print(frequencia.most_common(50))


#mostra as palavras unicas 
def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

palavrasunicastreinamento = buscapalavrasunicas(frequenciatreinamento)
palavrasunicasteste = buscapalavrasunicas(frequenciateste)
#print(palavrasunicastreinamento)


#extrai a palavra da frase que é passada e compara com a base
def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicastreinamento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

#caracteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])
#print(caracteristicasfrase)

basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento)
basecompletateste = nltk.classify.apply_features(extratorpalavras, frasescomstemmingteste)
#print(basecompleta[15])

# constroi a tabela de probabilidade
classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento)
print(classificador.labels())
#print(classificador.show_most_informative_features(20))

print(nltk.classify.accuracy(classificador, basecompletateste))

erros = []
for (frase, classe) in basecompletateste:
    #print(frase)
    #print(classe)
    resultado = classificador.classify(frase)
    if resultado != classe:
        erros.append((classe, resultado, frase))
#for (classe, resultado, frase) in erros:
#    print(classe, resultado, frase)

from nltk.metrics import ConfusionMatrix
esperado = []
previsto = []
for (frase, classe) in basecompletateste:
    resultado = classificador.classify(frase)
    previsto.append(resultado)
    esperado.append(classe)

#esperado = 'alegria alegria alegria alegria medo medo surpresa surpresa'.split()
#previsto = 'alegria alegria medo surpresa medo medo medo surpresa'.split()
matriz = ConfusionMatrix(esperado, previsto)
print(matriz)

# 1. Cenário
# 2. Número de classes - 16%
# 3. ZeroRules - 21,05%

teste = 'eu sinto amor por voce'
testestemming = []
stemmer = nltk.stem.RSLPStemmer()
for (palavrastreinamento) in teste.split():
    comstem = [p for p in palavrastreinamento.split()]
    testestemming.append(str(stemmer.stem(comstem[0])))
#print(testestemming)

novo = extratorpalavras(testestemming)
#print(novo)

#print(classificador.classify(novo))
distribuicao = classificador.prob_classify(novo)
#for classe in distribuicao.samples():
#    print("%s: %f" % (classe, distribuicao.prob(classe)))










