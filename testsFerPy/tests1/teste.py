import re
import string

num_words = 0
frequency = {}
count = 0
match_pattern = []
k = 0  #somatorio 1
l = 0 #somatorio 2
x = 0
with open('analisando.txt', 'r') as document_text: # chamada do doc
# pega o conteudo do txt e transforma tudo em string com lower case
    text_string = document_text.read().lower()
# delimitação do tamanho das palavras q for querer
    match_pattern = re.findall(r'\b[a-z]{2,22}\b', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    
    #for words1 in frequency_list:
        #print(words1, frequency[words1]) #isso aki printa a frequencia de cada palavra no texto

#palavra = input("Enter word to be searched:")
    depressivoTxt = open('pronomes.txt', 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    depressivo = depressivoTxt.read()
    depressivoTxt.close()
    palavrasdepretxt = open('palavrasdepre.txt', 'r')
    palavrasdepre = palavrasdepretxt.read()
    palavrasdepretxt.close()
    filtrotxt = open('filtro.txt', 'r')
    filtro = filtrotxt.read()
    filtrotxt.close()
    palavraTeste = 'eu'
    document_text = open('analisando.txt', 'r')
    for line in document_text:
        words = line.split()
        num_words += len(words) #numero ttl d palavras
        
    #esse aki é o q funciona
    #for i in match_pattern :
     #   if(i == palavraTeste) :
      #      k = k+1    

    for i in match_pattern :
        if i in depressivo :
            k = k+1    
    
    for i in match_pattern :
        if i in palavrasdepre :
            l = l+1 

    for i in match_pattern :
        if i in filtro :
            x = x+1 
   
            
ttlwords = num_words-x
print(num_words, k, l, x )
print("Number of words:", ttlwords) #numero ttl de palavras no texto analisado
print("Occurrences of words(pronomes):", k) #frequencia das palavras que eu busco
print("porcentagem de palavras buscadas(pronomes):", (100*k)/ttlwords) #porcentagem
print("Occurrences of words(depre):", l)
print("porcentagem de palavras buscadas(depre):", (100*l)/ttlwords) 
print("porcentagem TTL:", (100*(k+l)/ttlwords))  



    