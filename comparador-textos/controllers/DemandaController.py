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
        # Buscar uma demanda com o mesmo id para verificar se já existe
        demanda = service.obter_demanda_por_id(nova_demanda.id_demanda)
        if demanda is not None:
            print("Demanda já existe!")
            service.excluir_demanda(demanda.id_demanda)
        service.criar_demanda(nova_demanda)
        return jsonify(nova_demanda.to_dict())

    @staticmethod
    def buscar_demandas_similares(demanda_id):
        id_demanda = demanda_id
        service = DemandaService()
        demanda = service.obter_demanda_por_id(id_demanda)
        if demanda is None:
            return jsonify({"message": "Demanda não encontrada!"})
        demandas = service.obter_todas_demandas()
        demandas_similares = encontrar_demandas_similares(demanda, demandas)

        resultado = []
        for demanda_similar in demandas_similares:
            resultado.append({
                "demanda": demanda_similar.demanda.to_dict(),
                "similaridade": demanda_similar.similaridade
            })

        return jsonify(resultado)

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
