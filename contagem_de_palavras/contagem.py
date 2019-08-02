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


def contandoCoisas(texto, palavrasArq):

    #TTL palavras sendo buscadas
    p = 0
    #TTL STOPWORDS
    s = 0
    
    #PRONOMES
    palavraTXT = open(palavrasArq, 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    palavra = palavraTXT.read()
    palavraTXT.close()
    
    #STOP WORDS PERSONALIZADAS
    stoptxt = open('filtro.txt', 'r')
    stop = stoptxt.read()
    stoptxt.close()

    #TOKENIZANDO
    palavra = Tokenize(palavra)
    stop = Tokenize(stop)
    texto = Tokenize(texto)

    #Stemmando
    palavra = Stemming(palavra)
    stop = Stemming(stop)
    texto = Stemming(texto)

    #PRINTANDO
    #print(pronome)
    #print(filtro)
    #print(stringao)

    #CONTANDO COISAS EFETIVAMENTE
    for i in texto :
        if i in palavra :
            p = p+1 

    for i in texto :
        if i in stop :
            s +=1 
     
    #TOTAL DE PALAVRAS
    ttlwords = len(texto)
    
    #MENOS AS STOP WORDS
    ttlwords = ttlwords - s

    print(p)
    #print(s)
    #print('ttlwords', ttlwords)
    return print(p/ttlwords)