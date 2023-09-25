# Lendo as variaveis 
a, b, c = map(float, input().split())

# a sempre tem que ser o maior

if a >= b and a >= c :
    maior = a
    if b >= c :
        meio = b
        menor = c
    else:
        meio = c
        menor = b
if b >= a and b >= c:
    maior = b
    if a >= c:
        meio = a 
        menor = c 
    else:
        meio = c
        menor = a       
if c >= a and c >= b:
    maior = c
    if a >= c :
        meio = a
        menor = c
    else:
        meio = c
        menor = a


if maior >= meio + menor:
    print("NAO FORMA TRIANGULO") 
else:

    if maior ** 2 == meio ** 2 + menor ** 2 : 
        print("TRIANGULO RETANGULO")

    elif maior ** 2 > meio ** 2 + menor ** 2 :
        print("TRIANGULO OBTUSANGULO")

    elif maior ** 2 < meio ** 2 + menor ** 2 :
        print("TRIANGULO ACUTANGULO")

    if maior == meio == menor:
        print("TRIANGULO EQUILATERO")

    elif maior  == meio or maior == menor or meio == menor :
        print("TRIANGULO ISOSCELES")
        
        