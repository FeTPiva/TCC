import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao2

a = mineracaoemocao2.retornaEmocoes(1,2)
print(a)

  
def funcao(idPessoa, nTexto):
    j=1
    w=1
    primeira_coluna = []
    segunda_coluna = []
    vetor_saida  = mineracaoemocao2.retornaEmocoes(idPessoa,nTexto)
    for j in idPessoa:
        for w in nTexto:
            primeira_coluna = vetor_saida[0]
            segunda_coluna = vetor_saida[1]

            print(primeira_coluna)
        #print(segunda_coluna)

        j+=1




