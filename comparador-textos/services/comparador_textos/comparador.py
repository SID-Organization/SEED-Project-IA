import spacy
from models.entities.Demandas_similares import DemandaSimilar

nlp = spacy.load("pt_core_news_lg")


def processar_texto(texto):
    doc = nlp(texto)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)


def encontrar_demandas_similares(demanda, demandas):
    demandas_similares = []
    for demanda_existente in demandas:
        similaridade = comparar_demandas(demanda, demanda_existente)
        if similaridade > 0.9:
            if demanda.id_demanda == demanda_existente.id_demanda:
                continue
            obj_demanda_similar = DemandaSimilar(demanda_existente, similaridade)
            demandas_similares.append(obj_demanda_similar)
    return demandas_similares


def comparar_demandas(demanda1, demanda2):
    proposta_melhoria_demanda1 = processar_texto(demanda1.proposta_melhoria)
    descricao_qualitativo_demanda1 = processar_texto(demanda1.descricao_qualitativo)
    frequencia_uso_demanda1 = processar_texto(demanda1.frequencia_uso_demanda)
    situacao_atual_demanda1 = processar_texto(demanda1.situacao_atual_demanda)
    proposta_melhoria_demanda2 = processar_texto(demanda2.proposta_melhoria)
    descricao_qualitativo_demanda2 = processar_texto(demanda2.descricao_qualitativo)
    frequencia_uso_demanda2 = processar_texto(demanda2.frequencia_uso_demanda)
    situacao_atual_demanda2 = processar_texto(demanda2.situacao_atual_demanda)

    similaridade_proposta_melhoria = comparar_textos(proposta_melhoria_demanda1, proposta_melhoria_demanda2)
    print(similaridade_proposta_melhoria)
    similaridade_descricao_qualitativo = comparar_textos(descricao_qualitativo_demanda1, descricao_qualitativo_demanda2)
    print(similaridade_descricao_qualitativo)
    similaridade_frequencia_uso_demanda = comparar_textos(frequencia_uso_demanda1, frequencia_uso_demanda2)
    print(similaridade_frequencia_uso_demanda)
    similaridade_situacao_atual_demanda = comparar_textos(situacao_atual_demanda1, situacao_atual_demanda2)
    print(similaridade_situacao_atual_demanda)

    similaridade = (
                           similaridade_proposta_melhoria + similaridade_descricao_qualitativo + similaridade_frequencia_uso_demanda +
                           similaridade_situacao_atual_demanda
                   ) / 4
    print(similaridade)
    return similaridade


def comparar_textos(texto1, texto2):
    doc1 = nlp(texto1)
    doc2 = nlp(texto2)
    similaridade = doc1.similarity(doc2)

    return similaridade
