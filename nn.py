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
def criaLista(val1, val2, val3):
    lista = []
    lista.insert(0, val1)
    lista.insert(1,val2)
    lista.insert(2, val3)
   
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
def retornaContagemTeste(idPessoa, txtPronomes, txtAbsolutas, txtTristes):
    pessoa = idPessoa+1
    texto = ConnectionDB.obterLinhaTextoxTeste(pessoa)
    
    textoTratado1 = contagem.contandoCoisas(texto ,pronome)
    textoTratado2 = contagem.contandoCoisas(texto,absoluta)
    textoTratado3 = contagem.contandoCoisas(texto,triste)

    #print(textoTratado1, textoTratado2, textoTratado3, idDepre)
    lista = criaLista(textoTratado1, textoTratado2, textoTratado3)
    #print("Contei palavras {} vezes = nPessoas".format(pessoa))
    return lista


a = retornaContagemTeste(1, pronome, absoluta, triste)
i=0
for i in a:
    print(a)