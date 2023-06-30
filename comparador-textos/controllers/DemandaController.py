from flask import request, jsonify
from models.entities.Demanda import Demanda
from services.comparador_textos.comparador import comparar_textos, encontrar_demandas_similares, comparar_demandas
from services.DemandaService import DemandaService


class DemandaController:
    def __init__(self):
        pass

    @staticmethod
    def criar_demanda():
        service = DemandaService()
        data = request.get_json()
        print("Dados recebidos: ", data)
        nova_demanda = Demanda(**data)
        print("Demanda criada: ", nova_demanda)
        service.criar_demanda(nova_demanda)
        return jsonify(nova_demanda.to_dict())

    @staticmethod
    def buscar_demandas_similares():
        # Pegar o id da demanda do body
        data = request.get_json()
        service = DemandaService()
        print(data)
        demanda1 = service.obter_demanda_por_id(data['demanda1'])
        demanda2 = service.obter_demanda_por_id(data['demanda2'])
        similaridade = comparar_demandas(demanda1, demanda2)
        if similaridade > 0.7:
            print("Demanda similar encontrada", similaridade)
            similaridade_string = str(similaridade)
            return similaridade_string
        else:
            print("Demanda similar não encontrada")
            similaridade_string = str(similaridade)
            return similaridade_string

    @staticmethod
    def listar_demandas():
        service = DemandaService()
        demandas = service.obter_todas_demandas()
        return jsonify([demanda.to_dict() for demanda in demandas])

    @staticmethod
    def obter_demanda(demanda_id):
        id_demanda = demanda_id
        service = DemandaService()
        demanda = service.obter_demanda_por_id(id_demanda)
        return jsonify(demanda.to_dict())

    @staticmethod
    def atualizar_demanda(demanda_id):
        id_demanda = demanda_id
        service = DemandaService()
        demanda_antiga = service.obter_demanda_por_id(id_demanda)
        data = request.get_json()
        demanda_atualizada = Demanda(**data)
        demanda_atualizada.id_demanda = demanda_antiga.id_demanda
        service.atualizar_demanda(demanda_atualizada)
        return jsonify(demanda_atualizada.to_dict())

    @staticmethod
    def excluir_demanda(demanda_id):
        id_demanda = demanda_id
        service = DemandaService()
        service.excluir_demanda(id_demanda)
        print(id_demanda)
        return jsonify({"message": "Demanda excluída com sucesso!"})
