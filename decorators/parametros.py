def meu_decorator(parametro1, parametro2):
    def decorator(funcao):
        def wrapper(*args, **kwargs):
            # Aqui você pode acessar os parâmetros passados para o decorator
            print("Parâmetro 1:", parametro1)
            print("Parâmetro 2:", parametro2)
            # Aqui você pode manipular os parâmetros da função
            # antes de chamar a função original
            resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return decorator

@meu_decorator("valor1", "valor2")
def minha_funcao(nome):
    print("Nome:", nome)

# Chamando a função decorada
minha_funcao("João")