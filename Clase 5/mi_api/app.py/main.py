#!/usr/bin/env python3
from flask import Flask
from login import login

app = Flask(__name__)

#servicios rest
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola mundo'

if __name__ == "__main__":

    app.run(host = '0.0.0.0', debug = True, port = 8081)
    app.run(debug = True)
    
from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get ('password')

    codRes, menRes, accion = inicializarVariables(user, password)

    salida = {
        'codRes' : codRes,
        'menRes' : menRes,
        'usuario' : user, 
        'accion' : accion
    }

    return jsonify(salida)