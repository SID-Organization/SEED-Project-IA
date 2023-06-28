from difflib import SequenceMatcher
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def processar_texto(texto):
    vetorizador = CountVectorizer()
    bow = vetorizador.fit_transform([texto])
    return bow


def encontrar_demandas_similares(demanda, demandas):
    demandas_similares = []
    for demanda_existente in demandas:
        similaridade = comparar_demandas(demanda, demanda_existente)
        if similaridade > 0.7:
            demandas_similares.append(demanda_existente)
    return demandas_similares


def comparar_demandas(demanda1, demanda2):
    bow_proposta_melhoria_demanda1 = processar_texto([demanda1.proposta_melhoria])
    bow_descricao_qualitativo_demanda1 = processar_texto([demanda1.descricao_qualitativo])
    bow_frequencia_uso_demanda1 = processar_texto([demanda1.frequencia_uso_demanda])
    bow_situacao_atual_demanda1 = processar_texto([demanda1.situacao_atual_demanda])
    bow_proposta_melhoria_demanda2 = processar_texto([demanda2.proposta_melhoria])
    bow_descricao_qualitativo_demanda2 = processar_texto([demanda2.descricao_qualitativo])
    bow_frequencia_uso_demanda2 = processar_texto([demanda2.frequencia_uso_demanda])
    bow_situacao_atual_demanda2 = processar_texto([demanda2.situacao_atual_demanda])

    similaridade_proposta_melhoria = comparar_textos(bow_proposta_melhoria_demanda1, bow_proposta_melhoria_demanda2)
    print(similaridade_proposta_melhoria)
    similaridade_descricao_qualitativo = comparar_textos(bow_descricao_qualitativo_demanda1,
                                                         bow_descricao_qualitativo_demanda2)
    print(similaridade_descricao_qualitativo)
    similaridade_frequencia_uso_demanda = comparar_textos(bow_frequencia_uso_demanda1, bow_frequencia_uso_demanda2)
    print(similaridade_frequencia_uso_demanda)
    similaridade_situacao_atual_demanda = comparar_textos(bow_situacao_atual_demanda1, bow_situacao_atual_demanda2)
    print(similaridade_situacao_atual_demanda)

    similaridade = (
                           similaridade_proposta_melhoria + similaridade_descricao_qualitativo + similaridade_frequencia_uso_demanda + similaridade_situacao_atual_demanda) / 4
    print(similaridade)
    return similaridade


def comparar_textos(bow1, bow2):
    similaridade = cosine_similarity(bow1, bow2)[0][0]
    return similaridade
