# Lendo as variáveis a, b, c

a, b, c = map(float, input().split())

# Definindo a condição e imprimindo os resultados

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b) :
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = (((a + b) * c )/2)
    print(f"Area = {area:.1f}")