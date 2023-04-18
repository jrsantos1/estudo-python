

lista_restornos = [100, 85, 82, 95, 104, 110, 103, 109, 92, 88, 95, 102]


valor_maximo_dd_atual = 0
valor_maximo = 0
valor_maximo_iteracao = 0
valor_minimo = 0
valor_minimo_iteracao = 0

def calcula_mdd(lista: list):
    mdd_lista = []
    for i in range(len(lista)):
        if i == len(lista):
            break
        valor_atual = 0
        valor = lista[i]
        list = lista[i+1:]
        for value in list:
            if value < valor and valor > valor_atual:
                valor_atual = valor / value - 1
                mdd_lista.append(valor_atual)
            else:
                mdd_lista.append(0)
    return max(mdd_lista)

mdd = calcula_mdd(lista_restornos)
print(mdd)


