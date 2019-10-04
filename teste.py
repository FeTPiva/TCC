import nn as classXTeste

pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'

a = classXTeste.retornaContagem(1, pronome, absoluta, triste)
print(a)