import csv

with open("arquivos/PESSOAS.2023") as file:
    for registro in csv.reader(file):
        print(registro)

