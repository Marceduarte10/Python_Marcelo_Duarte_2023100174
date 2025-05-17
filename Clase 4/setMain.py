#!/usr/bin/env python
#-*- Coding: utf-8 -*-
#Linea shebang: permite ejecutar este script directamente en sistemas Unix/Linux
#Codificacion UTF-8 para permitir carateres especiales

from flask import Flask, jsonify, request
#importamos Flask para crear la app web, jsonfy para devolver respuestas en JSON
#y request para manejar datos entrantes (por ejemplo, de formularios o JSON)

app = Flask (__name__)
#Creamos la instancia de la aplicacion Flask

@app.route('/', methods=['GET'])
def hello(): 
    #Definimos una ruta para el endpoint raiz "/" que responde a solicitudes GET
    return 'Hello World!'
    #Al acceder a la raiz del sitio, se devuelve este mensaje
if __name__ =="__main__":
    #Este bloque se ejecuta solo si el script se ejecuta directamente (no importado como modulo)

    ##app.run(host = '127.0.0.1', debug = True, port = 5000)
    #Linea comentada: ejecutaria el servidor localmente solo accesible desde la misma maquina

    app.run(host = '0.0.0.0', debug = True, port = 5000)
    #Ejecuta la app en el host 0.0.0.0, lo cual la hace accesible desde otras maquinas en la red
    #El modo debug permite ver errores detallados y reinicia el servidor al detectar cambios

    app.run(debug = True)
    # Esta linea esta de mas, ya que 'app.run' ya fue llamada antes.
    # En la practica, solo una llamada a 'app.run()' es necesaria.