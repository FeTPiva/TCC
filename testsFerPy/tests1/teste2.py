import re
import string

frequency = {}
document_text = open('teste.txt', 'r') #chamada do doc
text_string = document_text.read().lower() #pega o conteudo do txt e transforma tudo em string com lower case
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string) #delimitação do tamanho das palavras q for querer
 
for word in match_pattern:
    count = frequency.get(word,0) 
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print( words, frequency[words])