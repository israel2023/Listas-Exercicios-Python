# Lendo as variáveis A e B

a, b = map(int, input().split())

# Analisando qual a condição e imprimindo resultado

if a > b and a % b == 0 : 
    print(a)
    print(b)
    print("Sao Multiplos")

elif a < b and b % a == 0 :
    print("Sao Multiplos") 

elif a == b :
    print("Sao Multiplos")

else:   
    print("Nao sao Multiplos")  