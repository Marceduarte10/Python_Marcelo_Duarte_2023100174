#!/usr/bin/env python3
from flask import Flask
from login import login

app = Flask(__name__)

##servicios rest
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello ():
    return 'Hola mundo'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port = 5001)
    app.run(debug = True)



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
 