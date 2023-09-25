# Lendo as variaveis A, B e C

a, b, c = map(float, input().split())

# Calculando o valor de delta

delta = ((b**2) - 4 * a * c)

# calculando as raizes e imprimindo resultados

if delta >= 0  :
    
    if a != 0 :
        r1 = (- b + (delta**(1/2))) / (2 * a) 
        r2 = (- b - (delta**(1/2))) / (2 * a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")

# Determinando os casos impossiveis e imprimindo resultado

    elif a == 0 :
        print("Impossivel calcular")
elif delta < 0 :
    print("Impossivel calcular")




