import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print("Baixando o CSV")
        dados = entrada.read().decode("latin1")
        print("Download Completo")

        for cidade in csv.reader(dados.splitlines()):
            print(cidade)


if __name__ == '__main__':
    read('http://files.cod3r.com.br/curso-python/desafio-ibge.csv')