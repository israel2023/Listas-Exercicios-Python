# Lendo as coordenadas x e y
x, y = map(float, input().split())
# Definindo em qual quadrante se encontra o ponto e imprimindo resultados

if x > 0 and y > 0 :
    print("Q1")
elif x < 0 and y > 0 :
    print("Q2")
elif x < 0 and y < 0 :
    print("Q3")
elif x > 0 and y < 0 :
    print("Q4")
elif x == 0 and y == 0 :
    print("Origem")
elif x == 0 :
    print("Eixo Y")
elif y == 0 :
    print("Eixo X")

