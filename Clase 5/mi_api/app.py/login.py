from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')

    codRes, menRes, accion = inicializarVariables(user, password) # type: ignore

    salida = {
        'codRes' : codRes,
        'menRes' : menRes,
        'usuario' : user,
        'accion' : accion
    }
    return jsonify (salida)

    def inicializarVariables(user, password):
        userLocal = "mduarte"
        passLocal = "unida123"
        codRes = 'SIN_ERROR'
        menRes = 'OK'

        try: 
            print("Verificar login")
            if password == passLocal and user == userLocal:
                print("Usuario y contrasela OK")
                accion = "Success"
            else:
                print("Usuario o Contraseña incorrecta")
                accion = "Usuario o contraseña incorrecta"
                codRes = 'ERROR'
                menRes = 'Credenciales del usuario incorrectas'


except Exception as e:
    print("ERROR", str(e))
    codRes = 'ERROR'
    menRes = 'Msg: ' + str(e)
    accion = "Eror interno"

return codRes, menRes, accion
 