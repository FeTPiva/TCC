import contagem
import re
import string

textoAnalisado = 'analisando.txt'
pronome = 'pronomes.txt'
absoluta = 'absoluta.txt'
triste = 'triste.txt'

# chamada do doc
with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

#pronomes (refazer)
contagem.contandoCoisas(minhaString, pronome)

#palavras absolutas (comletar mais)
contagem.contandoCoisas(minhaString, absoluta)

#contagem triste (ok)
contagem.contandoCoisas(minhaString, triste)