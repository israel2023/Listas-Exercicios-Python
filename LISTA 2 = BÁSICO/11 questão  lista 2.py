# Lendo a variavel 
valor=round(float(input()),2)

# Calculando a quantidade de notas 

# Notas de 100
nota100=int(valor//100)
valor-=nota100*100

# Notas de 50
nota50=int(valor//50)
valor-=nota50*50

# Notas de 20
nota20=int(valor//20)
valor-=nota20*20

# Notas de 10
nota10=int(valor//10)
valor-=nota10*10

# Notas de 5
nota5=int(valor//5)
valor-=nota5*5

# Notas de 2
nota2=int(valor//2)
valor-=nota2*2

# Calculando a quantidade de moeda

# Moedas de 1.00
moeda01=int(valor//1)
valor-=moeda01

# Calculando a quantidade de centavos

# Criando a variavel centavos
centavos=round(valor*100,0)

# Centavos de 0.50
centavos50=int(centavos//50)
centavos-=centavos50*50

# Centavos de 0.25
centavos25=int(centavos//25)
centavos-=centavos25*25

# Centavos de 0.10
centavos10=int(centavos//10)
centavos-=centavos10*10

# Centavos de 0.05
centavos005=int(centavos//5)
centavos-=centavos005*5

# Centavos de 0.01
centavos001=int(centavos//1)
                
# Imprimindo resultados das quantidades de cada notas, moedas e centavos
print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda01} moeda(s) de R$ 1.00")
print(f"{centavos50} moeda(s) de R$ 0.50")
print(f"{centavos25} moeda(s) de R$ 0.25")
print(f"{centavos10} moeda(s) de R$ 0.10")
print(f"{centavos005} moeda(s) de R$ 0.05")
print(f"{centavos001} moeda(s) de R$ 0.01")
