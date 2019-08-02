import contagem
import re
import string
import dictemp
import operator


#textoAnalisado = 'teste1.txt'
pronome = 'pronomes.txt'
absoluta = 'absoluta.txt'
triste = 'triste.txt'
superString = []


#meuDic = dictemp.enviaFraseProcessada()
#textoAnalisado = meuDic["texto"]
#depressividade = meuDic["isDepressivo"]

#print(textoAnalisado,depressividade)
mylist = dictemp.enviaFraseProcessada()

#for x in mylist:

#  print(x)

#for x in mylist:
#    superString = x["texto"]
a = map(operator.itemgetter("Text"), mylist)

print(a)

#################################################################
# chamada do doc - temp ate a pt do Felipe ficar ok
#with open(textoAnalisado, 'r') as document_text:
#    minhaString = document_text.read()

#pronomes 
#contagem.contandoCoisas(textoAnalisado, pronome)

#palavras absolutas 
#contagem.contandoCoisas(textoAnalisado, absoluta)

#contagem triste 
#contagem.contandoCoisas(textoAnalisado, triste)