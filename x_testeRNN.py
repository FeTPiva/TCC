import Pre_processamento.ConnectionDB as ConnectionDB
import contagem_de_palavras.contagem as contagem
import csv
import ExtracaodeEmocoesemTextos.mineracaoemocao2 as mineracaoemocao
import sys
import main_porMediaTodasLinhas
import mysql.connector
import Pre_processamento.Corretor as Corretor
# Conexao com Banco de Dados
import nltk

from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
import numpy as np
import os

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
    texto = ConnectionDB.obterLinhaTextoxTeste(pessoa)
    
    textoTratado1 = contagem.contandoCoisas(texto ,pronome)
    textoTratado2 = contagem.contandoCoisas(texto,absoluta)
    textoTratado3 = contagem.contandoCoisas(texto,triste)

    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3)
    #print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista


def xTeste(minhaString):
    idPessoa = 1

    contagem_palavras = retornaContagem(idPessoa, pronome, absoluta, triste)
    #vetor de sentimentos
    sentimentos = mineracaoemocao.retorna_Votacao_Emocao_Probabilidade_Por_Media_Geral(idPessoa)
    #juntando os dois
    probs = criaListaCsv(contagem_palavras[0], contagem_palavras[1], contagem_palavras[2], sentimentos[0], sentimentos[1], sentimentos[2], sentimentos[3], sentimentos[4], sentimentos[5], contagem_palavras[3])

    return probs
print(tf.__version__)
​print(keras.__version__)
​
#model = keras.models.load_model('./model.h5')
#print(os.path.join(os.path.dirname(__file__),'modelTiago.h5'))
​
​
app = Flask(__name__)
​

#decorator
@app.route('/previsao/', methods=['GET'])
@app.route('/previsao/m4', methods=['GET'])
def pred_wheater():
​
    RainToday = float(request.args.get('RainToday'))
    Humidity3pm = float(request.args.get('Humidity3pm'))
    Rainfall = float(request.args.get('Rainfall'))
    Humidity9am = float(request.args.get('Humidity9am'))
​
​
    model = keras.models.load_model(os.path.join(os.path.dirname(__file__),'modelTiago.h5'))
​
    x = np.array([[RainToday, Humidity3pm, Rainfall, Humidity9am]])
​
    y_pred = model.predict(x)
​
    if ( y_pred > 0.5 ):
        resp = {'prev':1}
    else:
        resp = {'prev':0}
​
    return jsonify(resp)
​

@app.route('/result', methods=['POST'])
def pred_depre():
    a = xTeste(minhaString) #lista com valores pra indicar depre
    

​
if __name__ == "__main__":
    app.run(debug=True)  
