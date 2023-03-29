import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = os.path.abspath(path=os.path.dirname(__file__)) + '\dados.csv'
df = pd.read_csv(path)
sexo = {'0': 'masculino', '1': 'feminino'}
df['Sexo'] = df['Sexo'].apply(lambda x: 'masculino' if x == 1 and x < 5 else 'feminino')
#df['Desenpenho'] = df.apply(lambda x: 'Excelente' if x['Anos de Estudo'] < 8 and x['Renda'] > 5000 else 'Médio')
df_mulheres = df.query('Sexo == "feminino"')
media_anos_de_estudo_mulheres = df.groupby(by=['Sexo', 'Anos de Estudo'], as_index=False).aggregate({'Renda': 'mean', 'Idade': 'mean'})
df_masulino = media_anos_de_estudo_mulheres.query("Sexo == 'masculino'")

sns.barplot(x='Anos de Estudo', y='Renda', data=df_masulino, color='b')
plt.show()

print(df)

