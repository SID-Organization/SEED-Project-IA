import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


def cria_objeto(demandas_list):
    demandas_por_dia = []  # Lista para armazenar as demandas por dia

    for demanda in demandas_list:
        data = demanda.data_criacao_demanda.date()  # Extrair apenas a parte da data
        quantidade_demandas = 1

        # Verificar se já existe um objeto com a mesma data
        demanda_existente = next((d for d in demandas_por_dia if d['data'] == data), None)

        if demanda_existente:
            demanda_existente['quantidade_demandas'] += quantidade_demandas
        else:
            demandas_por_dia.append({'data': data, 'quantidade_demandas': quantidade_demandas})

    return demandas_por_dia



def prever_criacao_demanda(demandas_list):
    data = cria_objeto(demandas_list)

    # Converter as datas para o formato adequado e criar um DataFrame
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'])  # Convertendo diretamente para datetime
    df.set_index('data', inplace=True)

    # Transformar o índice em um DatetimeIndex
    df.index = pd.DatetimeIndex(df.index)

    # Agrupar a contagem diária de demandas
    daily_count = df.resample('D').sum()

    # Ajustar o modelo ARIMA
    model = ARIMA(daily_count, order=(1, 0, 0))
    model_fit = model.fit()

    # Fazer previsões para os próximos 7 dias
    forecast = model_fit.forecast(steps=6)

    # Criar o objeto de previsão para os próximos dias
    previsao_proximos_dias = data
    for i in range(6):
        data = forecast.index[i].strftime("%a, %d %b %Y %H:%M:%S GMT")
        quantidade_demandas = int(forecast.values[i])
        previsao_proximos_dias.append({"data": data, "quantidade_demandas": quantidade_demandas})

    return previsao_proximos_dias


