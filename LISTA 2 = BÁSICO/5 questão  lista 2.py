# Lendo as variaveis uma a uma
x1,y1=input().split()
x2,y2=input().split()
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
# Calculando a distancia entre os pontos
Distancia=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
# Imprimindo resultado
print(f"{Distancia:.4f}")
