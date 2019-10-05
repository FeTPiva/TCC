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

#base de palavras de contagem
pronome = 'contagem_de_palavras/pronomes.txt'
absoluta = 'contagem_de_palavras/absoluta.txt'
triste = 'contagem_de_palavras/triste.txt'

#ok
def criaLista(val1, val2, val3, val4):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
    lista.insert(3, val4)
    return lista

#ok
def criaListaCsv(val1, val2, val3, val4, val5, val6, val7, val8, val9, isDepre):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
    lista.insert(3, val4)
    lista.insert(4, val5)
    lista.insert(5,val6)
    lista.insert(6, val7)
    lista.insert(7, val8)
    lista.insert(8, val9)
    lista.insert(9,isDepre)
    return lista

#ok
def retornaContagem(idPessoa, txtPronomes, txtAbsolutas, txtTristes):
    pessoa = idPessoa+1
    mylist = ConnectionDB.obterLinhaTexto(pessoa)
    #print(mylist)
    primeiroParse = mylist[0]
    #print(primeiroParse)
    segundoParse = primeiroParse["texto"]
    idDepre = primeiroParse["isDepressivo"]
    #print(segundoParse)

    textoTratado1 = contagem.contandoCoisas(segundoParse,pronome)
    textoTratado2 = contagem.contandoCoisas(segundoParse,absoluta)
    textoTratado3 = contagem.contandoCoisas(segundoParse,triste)

    
    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3, idDepre)
    #print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista

#Total de pessoas da base de dados para iterar
c = ConnectionDB.totalPessoas()


#iterator
x=0

#loop principal
while x < c:
    #print('estou no registro: ', x)
    #vetor de contagem
    progress(x, c, 'processado')
    contagem_palavras = retornaContagem(x, pronome, absoluta, triste)
    #vetor de sentimentos
    sentimentos = mineracaoemocao.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral(x)
    #juntando os dois
    probs_csv = criaListaCsv(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos[0], sentimentos[1], sentimentos[2], sentimentos[3], sentimentos[4], sentimentos[5], contagem_palavras[3])

    #gerando o csv    
    with open('resultados_pre_processamento/resultados.csv', 'a', newline = '') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(probs_csv)
    
    
    x+=1

print("Terminado!")