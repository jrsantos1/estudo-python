import requests
import numpy as np


a = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(a[a>5])

valorAplicado = np.array([5000, 6000, 7000, 8000])
taxaJuros = np.array([1, 2, 3, 4])
resultado = valorAplicado * taxaJuros
print(resultado)

exit()

def get_ids_cervejarias():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    if r.status_code == 200:
        return [r['id'] for r in r.json()]


def get_ids_cervejarias_complete():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    return r


print("Pegar dados segregados com for")

print(get_ids_cervejarias())

print("Pegar dados completos")

print(get_ids_cervejarias_complete().json())

