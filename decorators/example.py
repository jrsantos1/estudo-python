import time
from datetime import date

def calcular_tempo(valor1, valor2):
    def decorator(funcao):
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            print(valor1)
            print(valor2)
            print('inciando calculo')
            inicio = time.time()
            funcao('texto')
            time.sleep(5)
            print(time.time() - inicio)
            return funcao
        return wrapper
    return decorator

@calcular_tempo("parametro1", "parametro2")
def mostrar_dia(texto: str):
    print(date.today())

mostrar_dia('teste', 4, 6, nome='jhonatan', sobrenome='ribeiro')