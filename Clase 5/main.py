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