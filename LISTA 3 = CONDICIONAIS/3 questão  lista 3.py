# Lendo um numero qualquer
n=float(input())
# Processando qual a condição e imprimindo os resultados
if n < 0 or n > 100 :
    print("Fora de intervalo")
elif n <= 25 :
    print("Intervalo [0,25]") 
elif n <= 50 :
    print("Intervalo (25,50]")
elif n <= 75 :
    print("Intervalo (50,75]")
elif n <= 100 :
    print("Intervalo (75,100]")      
