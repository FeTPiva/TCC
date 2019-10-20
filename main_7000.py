import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao7
import ExtracaodeEmocoesemTextos.mineracao_emocao3 as mineracaoemocao3
import contagem_de_palavras.polaridade as polaridade
import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
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
#c = ConnectionDB.totalTextos()
#print(c)
c = 7205
#iterator
x=2375

#loop principal

while x < c:
    contagem_palavras = []
    sentimentos7= []
    sentimentos3 = []
    sentimentos3v2 = []
    pol = 0

        
    progress(x, c, 'processado')
    
    contagem_palavras =  contagem.retornaContagem7000(x)
    #print(contagem_palavras)
    pol = polaridade.polarizando7000(x)

    sentimentos7 = mineracaoemocao7.retorna_sent_frase_7000(x)
    sentimentos3v2 = mineracaoemocao3.retornaVetor001_7000(x)
    sentimentos3 = mineracaoemocao3.retornaVetorProb7000(x)
 
    
    #juntando a macaronada
    probs_csv = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos7[0], sentimentos7[1],sentimentos7[2],sentimentos7[3],sentimentos7[4],sentimentos7[5], sentimentos3[0], sentimentos3[1], sentimentos3[2],sentimentos3v2[0],sentimentos3v2[1],sentimentos3v2[2], pol, contagem_palavras[3])

    #gerando o csv    
    with open('resultados_pre_processamento/resultados_teste7000.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(probs_csv)   
    
    x+=1

print("Terminado!")
