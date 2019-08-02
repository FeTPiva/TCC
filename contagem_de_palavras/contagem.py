import nltk
from nltk.stem import RSLPStemmer

#nltk.download() punkt e rslp

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


def contandoCoisas(stringao, arquivo2):

    #TTL PRONOMES
    p = 0
    #TTL STOPWORDS
    s = 0
    
    #PRONOMES
    pronomeTxt = open(arquivo2, 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    pronome = pronomeTxt.read()
    pronomeTxt.close()
    
    #STOP WORDS PERSONALIZADAS
    filtrotxt = open('filtro.txt', 'r')
    filtro = filtrotxt.read()
    filtrotxt.close()

    #TOKENIZANDO
    pronome = Tokenize(pronome)
    filtro = Tokenize(filtro)
    stringao = Tokenize(stringao)

    #Stemmando
    pronome = Stemming(pronome)
    filtro = Stemming(filtro)
    stringao = Stemming(stringao)

    #PRINTANDO
    #print(pronome)
    #print(filtro)
    print(stringao)

    #CONTANDO COISAS EFETIVAMENTE
    for i in stringao :
        if i in pronome :
            p = p+1 

    for i in stringao :
        if i in filtro :
            s +=1 
     
    #TOTAL DE PALAVRAS
    ttlwords = len(stringao)
    
    #MENOS AS STOP WORDS
    ttlwords = ttlwords - s

    print(p)
    #print(s)
    #print('ttlwords', ttlwords)
    return print(p/ttlwords)