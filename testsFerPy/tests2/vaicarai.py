import nltk
from nltk.stem import RSLPStemmer

#nltk.download() punkt

def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase


frase1 = "teste tentando correndo correr"
frase2 = "absoluto absolutamente"
frase1 = Tokenize(frase1)
frase2 = Tokenize(frase2)
print(frase1)
print(frase2)


frase1 = Stemming(frase1)
frase2 = Stemming(frase2)
print(frase1)
print(frase2)

