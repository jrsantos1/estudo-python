with open('../arquivos/pessoas.csv') as entrada:
  with open('../arquivos/pessoas.txt', 'w') as saida:
      for registro in entrada:
          pessoa = registro.strip().split(',')
          print('Nome: {} Idade: {}'.format(*pessoa), file=saida)
          print("teste", file=saida)