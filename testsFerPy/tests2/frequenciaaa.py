import re
import string
import nltk


def retornoFrequenciaa(minhaString):
    num_words = 0 #int
    frequency = {} #list
    count = 0 #iterator
    match_pattern = [] #leitura de palavras por regex
    k = 0  #somatorio 1
    l = 0 #somatorio 2 ..
    x = 0
    z = 0
    y = 0
    stemList = {}

    stemmer = nltk.stem.RSLPStemmer()
    text_string = minhaString.lower() #minusculass
    

    # delimitação do tamanho das palavras q for querer (2-22 no caso)
    # match pattern=palavras do meu texto sem espaço e tudo mais, é do tipo list
    match_pattern = re.findall(r'\b[a-z]{2,22}\b', text_string)

    #usar esse for se eu for querer printar as palavras do texto
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    
    #for words1 in frequency_list:
        #print(words1, frequency[words1]) #isso aki printa a frequencia de cada palavra no texto

#palavra = input("Enter word to be searched:")
    pronomeTxt = open('pronomes.txt', 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    pronome = pronomeTxt.read()
    pronomeTxt.close()
    palavrasdepretxt = open('palavrasdepre.txt', 'r')
    palavrasdepre = palavrasdepretxt.read()
    palavrasdepretxt.close()
    filtrotxt = open('filtro.txt', 'r')
    filtro = filtrotxt.read()
    filtrotxt.close()
    absolutatxt = open('absoluta.txt', 'r')
    absoluta = absolutatxt.read()
    absolutatxt.close()
    tristetxt = open('triste.txt', 'r')
    triste = tristetxt.read()
    tristetxt.close()
    
    #contagem ttl de palavras    
    num_words = len(match_pattern)
    
        
    #esse aki é o q funciona (MODELO)
    #for i in match_pattern :
     #   if(i == palavraTeste) :
      #      k = k+1    

    for i in match_pattern :
        stemList = stemmer.stem(i)
        print(stemList)
        for j in stemList :
            if j in pronome :
                k = k+1  
                
    
    for i in match_pattern :
        if i in palavrasdepre :
            l = l+1 

    for i in match_pattern :
        if i in filtro :
            x = x+1 
    
    for i in match_pattern :
        if i in absoluta:
            z = z+1 

    for i in match_pattern :
        if i in triste:
            y = y+1 
                   
    ttlwords = num_words-x
     
    
    print(k)
    return print((k+l+z+y)/ttlwords )
