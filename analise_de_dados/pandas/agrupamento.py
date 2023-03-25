import pandas as pd

dados = {
    'pessoa': ['jhonatan', 'francisco', 'marcos', 'jhonatan', 'francisco', 'fred'],
    'venda_valor': [20,304,5043,302,20, 400]
}

df = pd.DataFrame(data=dados)
df = df.groupby(by=['pessoa'], as_index=False).agg({'venda_valor': ['sum', 'mean']})
print(type(df))
print(df)