import contagem
import re
import string
import Pre_processamento.Corretor as Corretor


# chamada do doc - temp ate a pt do Felipe ficar ok

with open(textoAnalisado, 'r') as document_text:
    minhaString = document_text.read()

#pronomes 
p = contagem.contandoCoisasPrint(minhaString, pronome)

#palavras absolutas 
a = contagem.contandoCoisasPrint(minhaString, absoluta)

#contagem triste 
t = contagem.contandoCoisasPrint(minhaString, triste)



teste = contagem.criaLista(p, a, t)
print(teste)