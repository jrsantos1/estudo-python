import csv

with open("../arquivos/pessoas.csv") as arquivo:
    for registro in csv.reader(arquivo):
        print("Nome: {} Idade: {}".format(*registro))