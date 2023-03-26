
arquivo = open("arquivos/pessoas.csv")

try:
    for registro in arquivo:
        print("Nome: {} Sobrenome{}".format(*registro.split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print("O arquivo já foi fechado")