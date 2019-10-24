from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
import os
import numpy as np
from flask_cors import CORS
import backTestes as bt
import Pre_processamento.ConnectionDB as ConnectionDB

print(tf.__version__)
print(keras.__version__)
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/depressao', methods=['POST'])
def get_predict():
  result = 0.0
  erro = ""
  status_code = 200
  try:
    data = request.get_json()
    print(data["frases"])
    if len(data["frases"]) > 0:
        result = bt.predictKeras(bt.geraVetorResultados2(data["frases"]))
        print(result)
    else:
        erro = {"Message": "Erro ao ler JSON... Algum atributo está inválido!"}
        status_code = 400
        return erro, status_code 
  except Exception as Ex:
    print(Ex)
    return {"Exception": "Error"}
  return jsonify({"isDepressivo": float(result), "acuracia": 74.9}), 200

@app.route('/getFrases', methods=['POST'])
def getFrases():
  data = request.get_json()
  id = 237
  idKeras = id - 234
  textos = ConnectionDB.retornaTextosGeralTeste(id)
  result = bt.predictKerasbyId(idKeras) 
  return jsonify({"frases":textos,"acuracia": 74.9, "isDepressivo": float(result)}), 200
if __name__ == '__main__':
  app.run(debug=True)