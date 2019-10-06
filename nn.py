import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao
import Pre_processamento.Corretor as Corretor
# Conexao com Banco de Dados
import nltk


#ok 
def criaLista(val1, val2, val3):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
   
    return lista

#ok
def criaListaCsv2(val1, val2, val3, val4, val5, val6, val7, val8, val9):
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
    
    return lista

#ok
def retornaContagemTeste(idPessoa):
    pronome = 'contagem_de_palavras/pronomes.txt'
    absoluta = 'contagem_de_palavras/absoluta.txt'
    triste = 'contagem_de_palavras/triste.txt'
    pessoa = idPessoa+1
    texto = ConnectionDB.obterLinhaTextoxTeste(pessoa)
    
    textoTratado1 = contagem.contandoCoisas(texto ,pronome)
    textoTratado2 = contagem.contandoCoisas(texto,absoluta)
    textoTratado3 = contagem.contandoCoisas(texto,triste)

    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3)
    #print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista


def geraVetorResultados():
    
    contagem_palavras = retornaContagemTeste(0)

    sentimentos = mineracaoemocao.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral_xTeste(0)
    #juntando os dois
    probs_teste = criaListaCsv2(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos[0], sentimentos[1], sentimentos[2], sentimentos[3], sentimentos[4], sentimentos[5])

    print(probs_teste)
    return probs_teste

a = geraVetorResultados()
