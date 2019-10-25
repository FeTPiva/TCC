from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
import os
import numpy as np
from flask_cors import CORS, cross_origin
import backTestes as bt
import Pre_processamento.ConnectionDB as ConnectionDB

print(tf.__version__)
print(keras.__version__)
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/depressao', methods=['POST'])
@cross_origin(origin='*')
def get_predict():
  result = 0.0
  erro = ""
  status_code = 200
  try:
    data = request.get_json()
    if len(data["frases"]) > 0:
        result = bt.predictKeras(bt.geraVetorResultados2(data["frases"]))
    else:
        erro = {"Message": "Erro ao ler JSON... Algum atributo está inválido!"}
        status_code = 400
        return erro, status_code 
  except Exception as Ex:
    print(Ex)
    return {"Exception": Ex}
  return jsonify({"isDepressivo": float(result), "acuracia": 74.9}), 200

@app.route('/getFrases/<int:id>', methods=['GET'])
@cross_origin(origin='*')
def getFrases(id):
  if id != None:
    idKeras = id - 233
    textos = ConnectionDB.retornaTextosGeralTeste(id)
    result = bt.predictKerasbyId(idKeras)
    return jsonify({"frases":textos,"acuracia": 74.9, "isDepressivo": float(result)}), 200
  else:
    return {"Message": "Erro ao ler JSON... Algum atributo está inválido!"}, 400
if __name__ == '__main__':
  app.run(debug=True)