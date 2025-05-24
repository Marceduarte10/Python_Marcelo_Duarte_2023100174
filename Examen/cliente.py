# cliente.py
from flask import Blueprint, request, jsonify

cliente_bp = Blueprint('cliente', __name__)

# Base de datos simulada
CLIENTES = {
            "5213457": 
                {
                "ci": "5213457", 
                "accion": "Success", 
                "codRes": "SIN_ERROR", 
                "menRes": "OK"}
            }

@cliente_bp.route('/cliente', methods=['POST'])
def obtener_cliente():
    data = request.get_json()
    ci = data.get("ci")

    if ci in CLIENTES:
        respuesta = CLIENTES[ci]
    else:
        respuesta = {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }

    return jsonify(respuesta)