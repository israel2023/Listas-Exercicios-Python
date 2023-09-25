# Lendo a variavel
segundos=int(input())
# Calculando segundos em horas, minutos e segundos
horas=segundos//3600
minutos=(segundos%3600)//60
segundos=(segundos%3600)%60
# Imprimindo resultado
print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")

