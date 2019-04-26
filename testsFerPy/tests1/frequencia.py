import re
import string

def calcFrequencia(textoAnalisado):
    num_words = 0
    frequency = {}
    with open(textoAnalisado, 'r') as document_text: # chamada do doc
# pega o conteudo do txt e transforma tudo em string com lower case
        text_string = document_text.read().lower()
# delimitação do tamanho das palavras q for querer
        match_pattern = re.findall(r'\b[a-z]{2,22}\b', text_string)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        frequency_list = frequency.keys()

        for words in frequency_list:
            print(words, frequency[words]) #isso aki printa a frequencia de cada palavra no texto

#palavra = input("Enter word to be searched:")
    depressivoTxt = open('pronomes.txt', 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    depressivo = depressivoTxt.read()
    palavrasdepretxt = open('palavrasdepre.txt', 'r')
    palavrasdepre = palavrasdepretxt.read()
    filtrotxt = open('filtro.txt', 'r')
    filtro = filtrotxt.read()

    with open(textoAnalisado, 'r') as f: #abrindo de novo o texto pra transformar ele em string e contar as palavras
        for line in f:
            words = line.split()
            num_words += len(words)
            k = 0 #somatorio 1
            l = 0 #somatorio 2
            x = 0
    # pt pra filtrar a palavra
        for j in range(len(depressivo)):
            for i in words:
                if(i == depressivo[j]):
                    k = k+1
        for a in range(len(palavrasdepre)):
            for m in words:
                if(m == palavrasdepre[a]):
                    l = l+1
        for b in range(len(filtro)):
            for n in words:
                if(n == filtro[b]):
                    x = x+1
                    #print(filtro[b])
            
    ttlwords = num_words-x
    print(num_words, k, l, x, ttlwords)
    print("Number of words:", ttlwords) #numero ttl de palavras no texto analisado
    print("Occurrences of words(pronomes):", k) #frequencia das palavras que eu busco
    print("porcentagem de palavras buscadas(pronomes):", (100*k)/ttlwords) #porcentagem
    print("Occurrences of words(depre):", l)
    print("porcentagem de palavras buscadas(depre):", (100*l)/ttlwords) 
    print("porcentagem TTL:", (100*(k+l)/ttlwords))  
    


def retornoFrequencia(textoAnalisado):
    num_words = 0
  #palavra = input("Enter word to be searched:")
    depressivoTxt = open('pronomes.txt', 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    depressivo = depressivoTxt.read()
    palavrasdepretxt = open('palavrasdepre.txt', 'r')
    palavrasdepre = palavrasdepretxt.read()
    filtrotxt = open('filtro.txt', 'r')
    filtro = filtrotxt.read()

    with open(textoAnalisado, 'r') as f: #abrindo de novo o texto pra transformar ele em string e contar as palavras
        for line in f:
            words = line.split()
            num_words += len(words)
            k = 0 #somatorio 1
            l = 0 #somatorio 2
            f = 0
    # pt pra filtrar a palavra
        for j in range(len(depressivo)):
            for i in words:
                if(i == depressivo[j]):
                    k = k+1
        for a in range(len(palavrasdepre)):
            for m in words:
                if(m == palavrasdepre[a]):
                    l = l+1
        for b in range(len(filtro)):
            for n in words:
                if(n == filtro[b]):
                    f = f+1
                    #print(filtro[b])
            
    ttlwords = num_words-f
  

    return (k+l)/ttlwords 
