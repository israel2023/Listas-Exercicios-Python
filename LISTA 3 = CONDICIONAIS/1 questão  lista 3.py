# Lendo os valores de a, b, c, d
a, b, c, d=map(int,input().split())
# Fazendo as comparaçoes e imprimindo os resultados
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
