# main.py
from flask import Flask
from cliente import cliente_bp

app = Flask(__name__)

# Registrar Blueprint
app.register_blueprint(cliente_bp)

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)