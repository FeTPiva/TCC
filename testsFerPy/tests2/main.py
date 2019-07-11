import frequenciaa
import re
import string

textoAnalisado = 'teste.txt'

# chamada do doc
with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

frequenciaa.retornoFrequenciaa(minhaString)

 