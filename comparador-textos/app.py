from flask import Flask
from flask_mysqldb import MySQL
from services.bdconection import configurar_banco_dados
from controllers.DemandaController import DemandaController

app = Flask(__name__)
configurar_banco_dados()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/demandas', methods=['POST'])
def criar_demanda():
    return DemandaController().criar_demanda()


if __name__ == '__main__':
    app.run()
