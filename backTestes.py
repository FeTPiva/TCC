import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import Pre_processamento.Corretor as Corretor
from keras.models import Sequential, load_model
import numpy as np
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao7
import ExtracaodeEmocoesemTextos.mineracao_emocao3 as mineracao_emocao3
import contagem_de_palavras.polaridade as polaridade
from sklearn.preprocessing import StandardScaler
import pandas as pd

 
def geraVetorResultados():
    #pega a função predefinida no banco de dds e ai retorna o vetor tratado
    
    contagem_palavras = contagem.retornaContagemTeste(0)

    sentimentos7 = mineracaoemocao7.retorna_Votacao_Emocao_Probabilidade_Por_Media_GeralTeste(0)
    #print(sentimentos7) 


    sentimentos3 = mineracao_emocao3.retornaVetorProbTeste(0)
    #print(sentimentos3) #ok 


    sentimentos3v2 = mineracao_emocao3.retornaVetor001Teste(0)
    #print(sentimentos3v2) #ok

    pol = polaridade.polarizandoTeste(0)
    #print(pol)
    
    #juntando a macaronada
    probs_teste = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos7[0], sentimentos7[1],sentimentos7[2],sentimentos7[3],sentimentos7[4],sentimentos7[5], sentimentos3[0], sentimentos3[1], sentimentos3[2],sentimentos3v2[0],sentimentos3v2[1],sentimentos3v2[2], pol)

    #print(probs_teste)
    return probs_teste

def geraVetorResultados2(vetor):
    contagem_palavras = contagem.retornaContagemTeste2(vetor)
    sentimentos7 = mineracaoemocao7.retorna_Votacao_Emocao_Probabilidade_Por_Media_GeralTeste2(vetor)
    sentimentos3 = mineracao_emocao3.retornaVetorProbTeste2(vetor)

    
    sentimentos3v2 = mineracao_emocao3.retornaVetor001Teste2(vetor)


    pol = polaridade.polarizandoTeste2(vetor)
    
    #juntando a macaronada
    probs_teste = contagem.criaLista(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos7[0], sentimentos7[1],sentimentos7[2],sentimentos7[3],sentimentos7[4],sentimentos7[5], sentimentos3[0], sentimentos3[1], sentimentos3[2],sentimentos3v2[0],sentimentos3v2[1],sentimentos3v2[2], pol)

    return probs_teste


def predictKeras(vetor):
    #o vetor ali é o q vem do pré processamneto(probs teste)
    lista = []
    
    model = load_model('models/model75.h5')
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    dft = pd.read_csv("resultados_pre_processamento/csv_de_teste.csv")
    xteste_ = dft.values[:, 0: 16] 
    yteste_ = dft.values[:, 16]

    lista = xteste_.tolist()
    lista.append(vetor)
    xteste_np = np.asarray(lista)

    sc = StandardScaler()
    xteste = sc.fit_transform(xteste_np)
    result_teste = model.predict(xteste)
    result_teste2 = model.predict(xteste)
    
    #mano se isso roda de primeira vou sair dando cambalhota pela maua
    #print(result_teste[54][0])
    #print( result_teste2[54][0])
    return result_teste[54][0]

def predictKerasbyId(id):
    #o vetor ali é o q vem do pré processamneto(probs teste)
    lista = []
    
    model = load_model('models/model75.h5')
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    dft = pd.read_csv("resultados_pre_processamento/csv_de_teste.csv")
    xteste_2 = dft.values[:, 0: 16] 
    yteste_ = dft.values[:, 16]

    sc = StandardScaler()
    xteste = sc.fit_transform(xteste_2)
    result_teste = model.predict(xteste)
    result_teste2 = model.predict_classes(xteste)
    #print(result_teste[id][0])
    return result_teste[id][0]


#a = geraVetorResultados()
#print(a)
#predictKeras(a)
#predictKerasbyId(0)