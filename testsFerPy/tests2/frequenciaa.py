import re
import string
import nltk

def common_elements(testlist, biglist):
    common = 0

    for x in testlist:

        if x in biglist:

            common += 1

    return common

def retornoFrequenciaa(minhaString):
    num_words = 0 #int
    frequency = {} #list
    count = 0 #iterator

    listTextoAlvo = [] #leitura de palavras por regex
    stemListTextoAlvo = []

    listPronome = []
    stemPronome = []

    listFiltro=[]
    stemFiltro=[]

    k = 0  #somatorio 1
    l = 0 #somatorio 2 ..
    x = 0
    z = 0
    y = 0
    j = 0
   
    stemmer = nltk.stem.RSLPStemmer()

    text_string = minhaString.lower() #minusculass
    
    #TEXTO ALVO
    
    # delimitação do tamanho das palavras q for querer (2-22 no caso)
    # match pattern=palavras do meu texto sem espaço e tudo mais, é do tipo list
    listTextoAlvo = re.findall(r'\b[a-z]{1,22}\b', text_string)
 
    
    #PRONOMES
    pronomeTxt = open('pronomes.txt', 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    pronome = pronomeTxt.read()
    pronomeTxt.close()
    listPronome = re.findall(r'\b[a-z]{1,22}\b', pronome)
    
    #STOP WORDS
    filtrotxt = open('filtro.txt', 'r')
    filtro = filtrotxt.read()
    filtrotxt.close()
    listFiltro= re.findall(r'\b[a-z]{1,22}\b', filtro)
    
   
    #contagem ttl de palavras    
    num_words = len(listTextoAlvo)
    
    
    #FORZAO
    for word_textoAlvo in listTextoAlvo:
        stemListTextoAlvo = stemmer.stem(word_textoAlvo)
        #print( stemList)ok
                  
        for word_pronome in listPronome :
            stemPronome = stemmer.stem(word_pronome)
            #print(stemPronome)
            k = common_elements(stemListTextoAlvo, stemPronome)
            x = common_elements(stemListTextoAlvo, listFiltro)
            

           
                                
    print(k)
    print(x)
    return print(k/num_words)

