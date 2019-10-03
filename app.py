from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

users = [
{
    "user": "fefe",
    "password": "fefe"
},
{
    "user": "dridri",
    "password": "dridri"
}
]
lista = [
    {
        "id":10,
        "nome":"Farofa",
        "preco":12.50
    },
    {
        "id":3, 
        "nome":"batata",
        "preco":200
    }
]
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg0NjI1NzQsIm5iZiI6MTU2ODQ2MjU3NCwianRpIjoiZWQ0YmUyNWQtNzBiMC00YWVhLWIwMjYtOWFmYWU3OTZmYjA3IiwiZXhwIjoxNTY4NDYzNDc0LCJpZGVudGl0eSI6ImZlZmUiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.aYC3GdNCkxizmR7MaIi6lXmM7JqdUbzShVIxBvwZm0I
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'dri123'
jwt = JWTManager(app)

@app.route('/auth', methods = ['POST'])
def auth():
    retorno = {"message":"Credencias inválidas!"}, 401
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    for i in users:
        if (i["user"] == username) and (i["password"] == password):
            access_token = create_access_token(identity=username)
            retorno = jsonify(access_token=access_token), 200
    return retorno
            

@app.route('/produtos', methods=['GET'])
@jwt_required
def get_produtos():
    prod_list = {"items" : lista}
    return jsonify(prod_list)

@app.route('/produto/<int:id>', methods=['GET'])
@jwt_required
def get_produto():
    prod = {"id": "nome"}
    for produto in lista:
        if produto["id"] == id:
            prod = produto
    return jsonify(prod)
    
if __name__ == '__main__':
    app.run(debug=True)