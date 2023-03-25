import pandas as pd
nome = 'wesley'

if nome == 'wesley' and len(nome) > 1 or True:
    print('é verdade')
else:
    print('é mentira')

exit()

resultados = [
{'codsac': 'fd1664', 'nav': 2000, 'metrica': 600},
{'codsac': 'fd1665', 'nav': 1800, 'metrica': 900},
{'codsac': 'fd1666', 'nav': 1200, 'metrica': 450},
{'codsac': 'fd1667', 'nav': 1450, 'metrica': 500},
{'codsac': 'fd1668', 'nav': 1300, 'metrica': 534},
{'codsac': 'fd1669', 'nav': 1710, 'metrica': 334}]

novoResultado = []

for resultado in resultados:

    nav = resultado['nav']  * 100
    metrica = resultado['metrica'] * 100

    resultado['nav'] = nav
    resultado['metrica'] = metrica

    novoResultado.append(resultado)

df = pd.DataFrame(data=novoResultado)

print(df)








