from flask import Flask
from controllers.DemandaController import DemandaController

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Comparador de demandas WEG'

@app.route('/demandas/', methods=['GET'])
def listar_demandas():
    controller = DemandaController()
    return controller.listar_demandas()

@app.route('/demandas/prever', methods=['GET'])
def prever_quantidade_demandas():
    controller = DemandaController()
    return controller.prever_quantidade_demandas()

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
