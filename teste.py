import contagem_de_palavras.contagem as contagem
import contagem_de_palavras.polaridade as polaridade
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao
import ExtracaodeEmocoesemTextos.mineracao_emocao3 as mineracaoemocao3
import Pre_processamento.ConnectionDB as ConnectionDB

vet = ["que dia bonito", "nossa estou tão feliz", "caramba meu", "eu eu eu "]
#a = contagem.retornaContagemTeste2(vet)
a = contagem.retornaContagem(286)
print(a)
