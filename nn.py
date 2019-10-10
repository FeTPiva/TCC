import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao
import Pre_processamento.Corretor as Corretor
import nltk
from keras.models import Sequential, load_model
import numpy as np

def geraVetorResultados():
    
    contagem_palavras = contagem.retornaContagem(0)
    

    sentimentos = mineracaoemocao.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral_xTeste(0)
    #juntando os dois
    probs_teste = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos[0], sentimentos[1], sentimentos[2], sentimentos[3], sentimentos[4], sentimentos[5])
    

    print(probs_teste)
    return probs_teste


def predictKeras(vetor):
    #o vetor ali é o q vem do pré processamneto(probs teste)
    test  = np.asarray(vetor)
    
    model = load_model('my_model.h5')

    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    result = model.predict(test)
    #mano se isso roda de primeira vou sair dando cambalhota pela maua
    print(result)
    return result

#a = geraVetorResultados()
