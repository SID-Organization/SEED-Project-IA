from flask import Flask
from services.bdconection import configurar_banco_dados
from controllers.DemandaController import DemandaController

app = Flask(__name__)
configurar_banco_dados()


@app.route('/')
def hello_world():  # put application's code here
    return 'Comparador de demandas WEG'


@app.route('/demandas/', methods=['GET'])
def listar_demandas():
    controller = DemandaController()
    return controller.listar_demandas()


@app.route('/demandas/similar/<int:demanda_id>', methods=['GET'])
def comparar_demandas(demanda_id):
    controller = DemandaController()
    return controller.buscar_demandas_similares(demanda_id)


@app.route('/demandas/<int:demanda_id>', methods=['GET'])
def obter_demanda(demanda_id):
    controller = DemandaController()
    return controller.obter_demanda(demanda_id)


if __name__ == '__main__':
    app.run()
