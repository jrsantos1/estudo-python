
import pandas as pd
from pandas_datareader import data
import yfinance as yf
import scipy.stats as scs
import numpy as np

tickers = ['PETR4.SA', 'VALE3.SA', 'BBAS3.SA']
ativos = yf.Tickers(tickers)
df = ativos.history(period='2y')
precos = df['Close']
precos = precos.reset_index()
precos_reb_diario = precos.copy()
preco_retornos = precos.copy()
preco_retornos[tickers] = preco_retornos[tickers].pct_change()
retornos = precos[tickers].pct_change()

pesos = [0.5, 0.3, 0.2]
def sem_reb(row, preco, retornos, pesos: list, ativos: list):
    data = row['Date']
    linha = preco[preco['Date'] == data].index
    ativo_peso = zip(ativos, pesos)
    total_carteira = []
    if linha == 0:
        for ativo in ativo_peso:
            row[ativo[0]] = ativo[1] * 100
        precos.iloc[linha] = row
        precos_reb_diario.iloc[linha] = row
    else:
        """
            Sem rebalanceamento 
        """
        posicao_retorno = linha
        posicao_preco = linha - 1
        retorno = retornos.iloc[posicao_retorno]
        preco = preco.iloc[posicao_preco]
        for ativo in ativo_peso:
            preco_ativo = list(preco[ativo[0]][posicao_preco])[0]
            retorno_ativo = list(retorno[ativo[0]][posicao_retorno])[0]
            valor_ativo = preco_ativo + (retorno_ativo * preco_ativo)
            row[ativo[0]] = valor_ativo
            total_carteira.append(valor_ativo)
        precos.iloc[linha] = row

        """
            Rebalanceamento diário 
        """
        total_carteira = sum(total_carteira)
        ativo_peso = zip(ativos, pesos)
        for ativo in ativo_peso:
            row[ativo[0]] = ativo[1] * total_carteira
        precos_reb_diario.iloc[linha] = row


precos.apply(lambda x: sem_reb(x, precos, retornos=retornos, pesos=pesos, ativos=tickers) ,axis=1)

print(precos)

# precos.to_excel('precos.xlsx')
# retornos.to_excel('retornos.xlsx')

# pesos = [.3, .3, .4]
#
# carteira_retornos = precos * pesos
