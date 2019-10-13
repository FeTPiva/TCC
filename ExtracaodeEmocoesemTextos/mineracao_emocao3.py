# -*- coding: utf-8 -*-
import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
import Pre_processamento.ConnectionDB as ConnectionDB


#Ler arquivo de dados e conta a quantidade de linhas
dataset = pd.read_csv('ExtracaodeEmocoesemTextos/Tweets_Mg.csv',encoding='utf-8')


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

def retornaVetorProb(idPessoa): 
    pessoa = idPessoa+1
    #print("estou na pessoa", pessoa)
    mylist = ConnectionDB.retornaNTextosGeral(pessoa)
    vetor_saida = []
    
    positivo = 0
    negativo = 0
    neutro = 0
    
    prob_positivo = 0
    prob_negativo = 0
    prob_neutro = 0
    
    probs = []
                    
    i=0
    nTextos = ConnectionDB.nmrTextosPorPessoa(pessoa)
    #print("nTextos da pessoa",nTextos)
    #print(mylist)
    
    while i < nTextos:
     #   print("to na iteração do while: ",i)
        
                
        primeiroParse = mylist[i]
        #print("primeiro parse", primeiroParse)
        
        segundoParse = primeiroParse["texto"]
        primeiroParse.clear()
        
        terceiroParse = [segundoParse]
        
        valor_de_treino = vectorizer.transform(terceiroParse)
        terceiroParse.clear()
        vetor_saida = modelo.predict_proba(valor_de_treino)
                
        positivo += vetor_saida[0][0]
        #print("passei pela iteracao {} da pessoa {}, valor alegrettl: {}".format(i, pessoa, alegria))
        negativo += vetor_saida[0][1]
        neutro += vetor_saida[0][2]
        vetor_saida = []
        #print("vet saida depois: ",vetor_saida)
        i+=1  

    mylist.clear()
        
    prob_positivo = positivo / nTextos
    #print("Alegria: {}, nTextos: {}, prob_alegr: {}".format(alegria, nTextos,  prob_alegria))
    prob_negativo = negativo / nTextos
    prob_neutro = neutro/nTextos
    probs = [prob_positivo, prob_negativo,prob_neutro]
    #print("probs = {}".format(probs))
       
    return probs


def retornaVetor001(idPessoa): 
    pessoa = idPessoa+1
    #print("estou na pessoa", pessoa)
    mylist = ConnectionDB.retornaNTextosGeral(pessoa)
    vetor_saida = []
    
    positivo = 0
    negativo = 0
    neutro = 0
    
    
    probs = []
                    
    i=0
    nTextos = ConnectionDB.nmrTextosPorPessoa(pessoa)
    #print("nTextos da pessoa",nTextos)
    #print(mylist)
    vetorTransformado = []
    
    while i < nTextos:
     #   print("to na iteração do while: ",i)
        
                
        primeiroParse = mylist[i]
        #print("primeiro parse", primeiroParse)
        
        segundoParse = primeiroParse["texto"]
        primeiroParse.clear()
        
        terceiroParse = [segundoParse]
        
        valor_de_treino = vectorizer.transform(terceiroParse)
        terceiroParse.clear()
        vetor_saida = modelo.predict_proba(valor_de_treino)
        vetor_saida_descente = [vetor_saida[0][0],vetor_saida[0][1],vetor_saida[0][2]]
        vetorTransformado = monta_vet_001(vetor_saida_descente)
                        
        positivo += vetorTransformado[0]
        negativo += vetorTransformado[1]
        neutro += vetorTransformado[2]
        vetor_saida = []
                
        i+=1  
    
    vetorTransformado.clear()
    mylist.clear()
      
    probs = [positivo, negativo, neutro]
           
    return probs

    
def monta_vet_001(valVetor):
    vetResult = []
    valVetor1 = valVetor[0]
    valVetor2 = valVetor[1]
    valVetor3 = valVetor[2]

    if (valVetor1>valVetor2 and valVetor1>valVetor3):
        vetResult = [1,0,0]
    elif (valVetor2>valVetor1 and valVetor2>valVetor3):
        vetResult = [0,1,0]
    elif (valVetor3>valVetor1 and valVetor3>valVetor2):
        vetResult = [0,0,1]
          
    return vetResult



# Separando tweets e suas classes
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values


#Gera o modelo
vectorizer = CountVectorizer(ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)


# Entrada das frases
#testes = ['a vida humana é bela, divina e infinitamente abundante assim como a natureza.quando somos gratos por estas manifestações da natureza tornamo-nos um com o todo! como num sopro divino, nos dissipamos juntamente com estes símbolos da natureza manifestados.não há mais o eu e nem o mim, há somente o nós namastê!']

# Fazendo a classificação com o modelo treinado.
#freq_testes = vectorizer.transform(testes)

#forma textual de mostrar o resultado
#print(modelo.predict(freq_testes))

#esse aki sãos os valores em %
#print(modelo.predict_proba(freq_testes))

'''
#Saída - apenas pra relacionar com o dict
dictemocao = {'Positivo':1,'Negativo':2,'Neutro':3}
vetorsaida = []
for classe in modelo.predict(freq_testes):
    vetorsaida.append(dictemocao.get(classe))
    #vetorsaida.append(max(max(modelo.predict_proba(freq_testes))))
  '''  
