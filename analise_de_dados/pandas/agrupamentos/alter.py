import pandas as pd


dados_df1 = [
    {'nome': 'banco_1', 'counter':'1', 'valor': 200},
    {'nome': 'banco_1', 'counter':'2', 'valor': 200},
    {'nome': 'banco_2', 'counter':'1', 'valor': 700},
    {'nome': 'banco_2', 'counter':'2', 'valor': 200},
    {'nome': 'banco_3', 'counter':'1', 'valor': 800},
    {'nome': 'banco_3', 'counter':'2', 'valor': 200},
    {'nome': 'banco_4',  'counter':'1','valor': 100},
    {'nome': 'banco_4', 'counter':'2', 'valor': 200},
]

dados_df2 = [
    {'nome': 'banco_1',  'counter':'1', 'valor': 400},
{'nome': 'banco_1', 'counter':'2', 'valor': 200},
    {'nome': 'banco_2', 'counter':'1', 'valor': 700},
    {'nome': 'banco_3', 'counter':'1', 'valor': 1000},
{'nome': 'banco_3', 'counter':'2', 'valor': 200},
    {'nome': 'banco_4', 'counter':'1', 'valor': 40},
{'nome': 'banco_4', 'counter':'2', 'valor': 200},
]


df1 = pd.DataFrame(data=dados_df1)
df1.rename(columns={'valor': 'CDS'}, inplace=True)

df2 = pd.DataFrame(data=dados_df2)
df2.rename(columns={'valor': 'SWAP'}, inplace=True)
df1 = df1.merge(df2, on=['nome', 'counter'])
df1['total'] = df1.apply(lambda x: x['CDS'] + x['SWAP'], axis=1)
pivot = pd.pivot_table(df1, index=['nome'], values='total', aggfunc='sum', margins=True, margins_name='Total')
df1_group = df1.groupby(by='nome', as_index=False).agg({'total': 'sum'})
print(df1)