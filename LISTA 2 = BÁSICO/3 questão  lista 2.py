# Lendo as variaveis a, b e c
a, b, c=input().split()
a=int(a)
b=int(b)
c=int(c)
# Calculando o maior numero
MaiorAB=(a+b+abs(a-b))/2
MaiorABC=(MaiorAB+c+abs(MaiorAB-c))/2
# imprimindo resultado do maior numero
print(f"{MaiorABC:.0f} eh o maior")

         
