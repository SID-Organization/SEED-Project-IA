from flask import request, jsonify
from models.entities.Demanda import Demanda
from services.comparador_textos.comparador import comparar_textos, encontrar_demandas_similares, comparar_demandas
from services.DemandaService import DemandaService


class DemandaController:
    def __init__(self):
        pass

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
            # Deixar apenas 2 casas depois da vírgula
            demanda_similar.similaridade = round(demanda_similar.similaridade, 2)
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
