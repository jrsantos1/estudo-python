import pandas as pd

nome = "Jhonatan"
sobrenome = "Ribeiro"

print("Meu nome é {} e meu sobrenome é {}".format(nome, sobrenome))


pessoas = [
    {'nome': 'jhonatan', 'sobrenome': 'ribeiro', 'idade': 16},
    {'nome': 'pedro', 'sobrenome': 'santos', 'idade': 15},
    {'nome': 'joaquin', 'sobrenome': 'vila', 'idade': 24},
    {'nome': 'francisco', 'sobrenome': 'caio', 'idade': 31},
    {'nome': 'marcelo', 'sobrenome': 'ferreira', 'idade': 43}]

df = pd.DataFrame(data=pessoas)

#for pessoa in df.items:
#    pessoa

for ik,pessoa in df.iterrows():
    pessoa['nome']

for pessoa in df.iteritems:
    pessoa