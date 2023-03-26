

with open("arquivos/pessoas.csv") as arquivo:
    for registro in arquivo:
        print("Nome: {} Sobrenome: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("O arquivo já foi fechado")