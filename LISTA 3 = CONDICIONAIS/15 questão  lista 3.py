# Lendo a variavel DDD
ddd = int(input())

# Determinando se o DDD está cadastrado e imprimindo 

if ddd != 61 and ddd != 71 and ddd != 11 and ddd != 21 and ddd !=32 and ddd != 19 and ddd != 27 and ddd != 31 :
    print("DDD nao cadastrado")

# Determinando a localidade de acordo com DDD cadastrado e imprimindo

else:
    
    if ddd == 61 :
        print("Brasilia")
    
    elif ddd == 71 :
        print("Salvador")
    elif ddd == 11 :
        print("Sao Paulo")
    elif ddd == 21 :
        print("Rio de Janeiro")
    elif ddd == 32 :
        print("Juiz de Fora")
    elif ddd == 19 :
        print("Campinas")
    elif ddd == 27 :
        print("Vitoria")
    elif ddd == 31 :
        print("Belo Horizonte")
