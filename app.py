from flask import Flask, request, jsonify
import mysql.connector
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
import os

db_buffer = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="depressao"
)

print(tf.__version__)
print(keras.__version__)
print(os.path.join(os.path.dirname(__file__),'modelDepre.h5'))
app = Flask(__name__)
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
def get_produto():
    i = 1
    erro = ""
    status_code = 200
    data = request.get_json()
    mycursor = db_buffer.cursor()
    drop = "TRUNCATE TABLE tbl_xteste"
    mycursor.execute(drop)
    db_buffer.commit()
    sql = "INSERT INTO tbl_xteste (idTexto,idPessoa,texto) VALUES (%s,1,%s)"
    if data["frases"].len() > 0 and data["pessoa"] != '':
        for frase in data["frase"]:
            val = (i,frase, data["pessoa"])
            mycursor.execute(sql, val)
            db_buffer.commit()
            print("Dados inseridos com sucesso!\n")
            i += 1
    else:
        erro = {"Message": "Erro ao ler JSON... Algum atributo está inválido!"}
        status_code = 400
        return jsonify(erro), status_code
    model = keras.models.load_model(os.path.join(os.path.dirname(__file__),'modelTiago.h5'))
    y_pred = model.predict(data["frase"])
    print(y_pred)

if __name__ == '__main__':
    app.run(debug=True)