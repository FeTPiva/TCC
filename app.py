from flask import Flask, request, jsonify
import mysql.connector
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
import os
import numpy as np
from flask_cors import CORS
import backTestes as bt
import Pre_processamento.ConnectionDB as ConnectionDB

db_buffer = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="depressao"
)

print(tf.__version__)
print(keras.__version__)
print(os.path.join(os.path.dirname(__file__),'modelTiago.h5'))
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.debug = True

# Retorno 
#{
#    "frases": [
#        "",
#        "",
#        "",
#        ...
#    ]
#}

@app.route('/depressao', methods=['POST'])
def get_predict():
    #i = 1
    #erro = ""
    #status_code = 200
    #data = request.get_json()
    #mycursor = db_buffer.cursor()
    #drop = "TRUNCATE TABLE tbl_xteste"
    #mycursor.execute(drop)
    #db_buffer.commit()
    #sql = "INSERT INTO tbl_xteste (idTexto,idPessoa,texto) VALUES (%s,1,%s)"
    #if len(data["frases"]) > 0:
    #    for frase in data["frases"]:
    #        val = (i,frase)
    #        mycursor.execute(sql, val)
    #        db_buffer.commit()
    #        print("Dados inseridos com sucesso!\n")
    #        i += 1
    #else:
    #    erro = {"Message": "Erro ao ler JSON... Algum atributo está inválido!"}
    #    status_code = 400
    #    return jsonify(erro), status_code
    #model = keras.models.load_model(os.path.join(os.path.dirname(__file__),'models/modelTiago.h5'))
    #frases = data["frases"]
    #Pré processamento, ver com a Fe amanhã
    #x_pred = np.array()
    #y_pred = model.predict()
    #print(x_pred.shape)
    #return {"msg" : "sucesso"},200


    #vetor com xteste do banco de dados - tipo assim, pra uma frase padrão q ta lá
    result = bt.predictKeras(bt.geraVetorResultados())
    

    algumVetorDoPreProcessamento = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    result2 = bt.predictKeras(algumVetorDoPreProcessamento)
    
    
    id = 234

    #textos pré pronto do db (tbl_xteste)
    textos = ConnectionDB.retornaNTextosGeralTeste(id)

    #vai retorna o valor de probabilidade da pessoa ter depre ou n  - usar no caso de frases pré-definidas
    result3 = bt.predictKerasbyId(id)


    return jsonify({"isDepressivo": result, "acuracia": 74.9}), 200
if __name__ == '__main__':
    app.run(debug=True)