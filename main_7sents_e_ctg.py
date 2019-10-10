import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import csv
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao
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
    #print('estou no registro: ', x)
    #vetor de contagem
    progress(x, c, 'processado')
    contagem_palavras = contagem.retornaContagem(x)
    
    #vetor de sentimentos
    sentimentos = mineracaoemocao.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral(x)
    #juntando os dois
    probs_csv = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos[0], sentimentos[1], sentimentos[2], sentimentos[3], sentimentos[4], sentimentos[5],  contagem_palavras[3])

    #gerando o csv    
    with open('resultados_pre_processamento/resultados233.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(probs_csv)   
    
    x+=1

print("Terminado!")

