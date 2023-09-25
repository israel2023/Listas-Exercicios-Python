# Lendo as variaveis
tempo_gasto=int(input())
velocidade_media=int(input())
# Calculando a distancia
distancia=tempo_gasto*velocidade_media
# Calculanco a quantidade de litros
litros=distancia/12
# Imprimindo resultado
print(f"{litros:.3f}")
