import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao2
import Pre_processamento.ConnectionDB as ConnectionDB

c = ConnectionDB.totalPessoas()
i=0

while i<c:
    #a = mineracaoemocao2.retornaProbabilidadeEmocoes(i, 2)
    pessoa = i+1
    #a = ConnectionDB.retornaNTextos(pessoa,2)
    
    a = mineracaoemocao2.retornaEmocoes(i, 2)
    print(a)
    i+=1
    