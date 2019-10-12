# -*- coding: utf-8 -*-

import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict


#Ler arquivo de dados e conta a quantidade de linhas
dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8')


#Conta a quantidade de linhas de tweets neutros, positivos e negativos
dataset.count()
dataset[dataset.Classificacao=='Neutro'].count()
dataset[dataset.Classificacao=='Positivo'].count()
dataset[dataset.Classificacao=='Negativo'].count()


#remove links, pontos, virgulas,ponto e virgulas, @ dos tweets
#coloca tudo em minusculo
def Preprocessamento(instancia):
    instancia = re.sub(r"http\S+", "", instancia).lower().replace(',','').replace('.','').replace(';','').replace('-','').replace(':','').replace('@','')
    return (instancia)


# Separando tweets e suas classes
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values


#Gera o modelo
vectorizer = CountVectorizer(ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)


# Entrada das frases
testes = ['Esse governo está no início, vamos ver o que vai dar']

# Fazendo a classificação com o modelo treinado.
freq_testes = vectorizer.transform(testes)
#print(modelo.predict(freq_testes))
#print(max(max(modelo.predict_proba(freq_testes))))

#Saída
dictemocao = {'Positivo':1,'Negativo':2,'Neutro':3}
vetorsaida = []
for classe in modelo.predict(freq_testes):
    vetorsaida.append(dictemocao.get(classe))
    vetorsaida.append(max(max(modelo.predict_proba(freq_testes))))
print(vetorsaida)
