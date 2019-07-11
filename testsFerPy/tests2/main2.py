import finalFrequencia
import re
import string

textoAnalisado = 'analisando.txt'

# chamada do doc
with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

finalFrequencia.contandoCoisas(minhaString)

#https://www.linkedin.com/pulse/classifica%C3%A7%C3%A3o-de-textos-em-python-luiz-felipe-araujo-nunes/ MUITO FODA