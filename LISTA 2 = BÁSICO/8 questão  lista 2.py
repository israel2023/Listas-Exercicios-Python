# Lendo a variavel e imprimindo valor
valor=int(input())
print(valor)
# Notas de 100
nota100=valor//100
valor=valor%100
# Notas de 50
nota50=valor//50
valor=valor%50
# Notas de 20
nota20=valor//20
valor=valor%20
# Notas de 10
nota10=valor//10
valor=valor%10
# Notas de 5
nota5=valor//5
valor=valor%5
# Notas de 2
nota2=valor//2
valor=valor%2
# Notas de 1
nota1=valor//1
valor=valor%1
# Imprimindo resultados
print(f"{nota100:.0f} nota(s) de R$ 100,00")
print(f"{nota50:.0f} nota(s) de R$ 50,00")
print(f"{nota20:.0f} nota(s) de R$ 20,00")
print(f"{nota10:.0f} nota(s) de R$ 10,00")
print(f"{nota5:.0f} nota(s) de R$ 5,00")
print(f"{nota2:.0f} nota(s) de R$ 2,00")
print(f"{nota1:.0f} nota(s) de R$ 1,00")
