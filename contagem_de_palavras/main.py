import contagem
import re
import string

textoAnalisado = 'analisando.txt'
pronome = 'pronomes.txt'
absoluta = 'absoluta.txt'
triste = 'triste.txt'


# chamada do doc - temp ate a pt do Felipe ficar ok
with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

#pronomes 
contagem.contandoCoisasPrint(minhaString, pronome)

#palavras absolutas 
contagem.contandoCoisasPrint(minhaString, absoluta)

#contagem triste 
contagem.contandoCoisasPrint(minhaString, triste)