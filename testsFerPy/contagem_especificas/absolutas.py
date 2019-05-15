import re
import string

def absolutFrequencia(textoAnalisado):
    num_words = 0
    frequency = {}
    count = 0
    match_pattern = []
    x = 0
    z = 0
    
    with open(textoAnalisado, 'r') as document_text: # chamada do doc
# pega o conteudo do txt e transforma tudo em string com lower case
        text_string = document_text.read().lower()
# delimitação do tamanho das palavras q for querer
        match_pattern = re.findall(r'\b[a-z]{2,22}\b', text_string)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        #frequency_list = frequency.keys()
    
    #for words1 in frequency_list:
        #print(words1, frequency[words1]) #isso aki printa a frequencia de cada palavra no texto

#palavra = input("Enter word to be searched:")
        
        filtrotxt = open('filtro.txt', 'r')
        filtro = filtrotxt.read()
        filtrotxt.close()
        absolutatxt = open('absoluta.txt', 'r')
        absoluta = absolutatxt.read()
        absolutatxt.close()
        palavraTeste = 'eu'

        document_text = open(textoAnalisado, 'r')
        for line in document_text:
            words = line.split()
            num_words += len(words) #numero ttl d palavras
           
        for i in match_pattern :
            if i in filtro :
                x = x+1 
    
        for i in match_pattern :
            if i in absoluta:
                z = z+1 
        
            
    ttlwords = num_words-x
    print(num_words, x, z )
    print("Number of words (sem as stop words):", ttlwords) #numero ttl de palavras no texto analisado
    print("Occurrences of words(absoluts):", z) 
    print("porcentagem de palavras buscadas(absoluts):", (100*z)/ttlwords) 
    
    
def retornoAbsolutFreq(textoAnalisado):
   num_words = 0
    frequency = {}
    count = 0
    match_pattern = []
    x = 0
    z = 0
    
    with open(textoAnalisado, 'r') as document_text: # chamada do doc
# pega o conteudo do txt e transforma tudo em string com lower case
        text_string = document_text.read().lower()
# delimitação do tamanho das palavras q for querer
        match_pattern = re.findall(r'\b[a-z]{2,22}\b', text_string)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        #frequency_list = frequency.keys()
    
    #for words1 in frequency_list:
        #print(words1, frequency[words1]) #isso aki printa a frequencia de cada palavra no texto

#palavra = input("Enter word to be searched:")
        
        filtrotxt = open('filtro.txt', 'r')
        filtro = filtrotxt.read()
        filtrotxt.close()
        absolutatxt = open('absoluta.txt', 'r')
        absoluta = absolutatxt.read()
        absolutatxt.close()
        palavraTeste = 'eu'

        document_text = open(textoAnalisado, 'r')
        for line in document_text:
            words = line.split()
            num_words += len(words) #numero ttl d palavras
           
        for i in match_pattern :
            if i in filtro :
                x = x+1 
    
        for i in match_pattern :
            if i in absoluta:
                z = z+1 
        
            
    ttlwords = num_words-x
  

    return (z)/ttlwords 
