
arquivo = open('arquivos/pessoas.csv')
dados = arquivo.read()
arquivo.close()

arquivo = open('arquivos/pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
  print('Nome: {} Sobrenome: {} Idade: {}'.format(*registro.split(',')))
