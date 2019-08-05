import contagem
import re
import string

textoAnalisado = 'contagem_de_palavras/analisando.txt'
pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'


# chamada do doc - temp ate a pt do Felipe ficar ok
with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

#pronomes 
contagem.contandoCoisasPrint(minhaString, pronome)

#palavras absolutas 
contagem.contandoCoisasPrint(minhaString, absoluta)

#contagem triste 
contagem.contandoCoisasPrint(minhaString, triste)