from cgi import print_arguments
import Lacos
import Forca



print("Bem vindo, selecione a opção desejada")
print ("___________________________")
print("(1) Adivinhação (2) Forca")

jogo = int(input("Opção desejada: "))

if(jogo == 1): 
    Lacos.jogar()
elif(jogo == 2): 
    Forca.jogar()
else: 
    print("Opção inválida! ")

