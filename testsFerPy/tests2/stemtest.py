import re
import nltk
import string

frequency = {} #list
match_pattern = [] #leitura de palavras por regex

#usar esse comando se for rodar esse cogido pela primeira vez, baixaro rslp
#nltk.download()

textoAnalisado = 'analisando.txt'

with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

#text_string= "teste absoluto rode por favor, absolutamente"

match_pattern = re.findall(r'\b[a-z]{2,22}\b', minhaString)

stemmer = nltk.stem.RSLPStemmer()

for word in match_pattern:
    frequency = stemmer.stem(word)
     
    print(frequency)