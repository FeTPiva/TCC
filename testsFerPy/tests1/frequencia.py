import re
import string

num_words = 0
frequency = {}
document_text = open('teste.txt', 'r')  # chamada do doc
# pega o conteudo do txt e transforma tudo em string com lower case
text_string = document_text.read().lower()
# delimitação do tamanho das palavras q for querer
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])
palavra = input("Enter word to be searched:")
#palavra = [palavras...]
with open('teste.txt', 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        k = 0
      #pt pra filtrar a palavra
       #for j -> palavra.leght, i==palavra[j]
       for i in words:
            if(i == palavra):
                k = k+1
print("Number of words:", num_words)
print("Occurrences of the word:", k)
