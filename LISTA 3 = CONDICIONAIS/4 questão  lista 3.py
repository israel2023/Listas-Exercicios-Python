# Lendo as variavéis 
codigo, quantidade=map(int,input().split())
# Definindo condição e imprimindo resultado
if codigo == 1 :
    cachorro_quente= 4.0
    total= quantidade * cachorro_quente
elif codigo == 2 :
    x_salada = 4.50
    total = quantidade * x_salada
elif codigo == 3 :
    x_bacon = 5.0
    total = quantidade * x_bacon
elif codigo == 4 :
    torrada_simples = 2.0
    total = quantidade * torrada_simples
elif codigo == 5 :
    refrigerante = 1.50
    total = quantidade * refrigerante
print(f"Total: R$ {total:.2f}")
    

    