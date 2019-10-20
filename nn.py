import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import Pre_processamento.Corretor as Corretor
import nltk
from keras.models import Sequential, load_model
import numpy as np
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao7
import ExtracaodeEmocoesemTextos.mineracao_emocao3 as mineracao_emocao3
import contagem_de_palavras.polaridade as polaridade

def geraVetorResultados():
    #pega a função predefinida no banco de dds e ai retorna o vetor tratado
    
    contagem_palavras = contagem.retornaContagem(0)

    sentimentos7 = mineracaoemocao7.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral(0)
    #print(sentimentos7) 


    sentimentos3 = mineracao_emocao3.retornaVetorProb(0)
    #print(sentimentos3) #ok


    sentimentos3v2 = mineracao_emocao3.retornaVetor001(0)
    #print(sentimentos3v2) #ok

    pol = polaridade.polarizando(0)
    #print(pol)
    
    #juntando a macaronada
    probs_teste = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos7[0], sentimentos7[1],sentimentos7[2],sentimentos7[3],sentimentos7[4],sentimentos7[5], sentimentos3[0], sentimentos3[1], sentimentos3[2],sentimentos3v2[0],sentimentos3v2[1],sentimentos3v2[2], pol)


    print(probs_teste)
    return probs_teste


def predictKeras(vetor):
    #o vetor ali é o q vem do pré processamneto(probs teste)
    vet1 = [vetor]
    test  = np.asarray(vet1)
    
    model = load_model('my_model.h5')

    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    result = model.predict(test)
    #mano se isso roda de primeira vou sair dando cambalhota pela maua
    print(result)
    return result

#a = geraVetorResultados()
