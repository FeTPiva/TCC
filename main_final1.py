import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao7
import ExtracaodeEmocoesemTextos.mineracao_emocao3 as mineracao_emocao3
import contagem_de_palavras.polaridade as polaridade

import csv
import sys

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '▓' * filled_len + '~' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s    %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  


print("Processando....")

#Total de pessoas da base de dados para iterar
c = ConnectionDB.totalPessoas()

#iterator
x=0

#loop principal

while x < c:
    contagem_palavras = []
    sentimentos = 0
    #print('estou no registro: ', x)

    #vetor de contagem
    progress(x, c, 'processado')
    contagem_palavras = contagem.retornaContagem(x)

    #vetor de sentimentos
    sentimentos7 = mineracaoemocao7.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral(x)

    #vetor3 sents_vini
    sentimentos3 = mineracao_emocao3....

    #polaridade
    pol = polaridade.polarizando(x)
    
    #vetor de sentimentos_meu (cagado)
    #sentimentos = sents.retorna_Votacao_3Emocoes(x)


    #juntando os dois
    probs_csv = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos,contagem_palavras[3])

    #gerando o csv    
    with open('resultados_pre_processamento/resultados_novo.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(probs_csv)   
    
    x+=1

print("Terminado!")
