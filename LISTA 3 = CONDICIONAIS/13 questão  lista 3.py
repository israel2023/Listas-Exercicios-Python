# Lendo a variavel salario

salario = float(input())

# Calculando um novo salario com um percetual para cada condição e imprimindo o novo salario, o reajuste e o percentual

if salario > 0 and salario <= 400.00 :
    novo_salario = salario + ((15 / 100) * salario)
    reajuste = novo_salario - salario 
    percentual = reajuste / (salario / 100)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual:.0f} %")
else:
    if salario >= 400.01 and salario <= 800.00 :
        novo_salario = salario + ((12 / 100) * salario)
        reajuste = novo_salario - salario 
        percentual = reajuste / (salario / 100)
        print(f"Novo salario: {novo_salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual:.0f} %")

    elif salario >= 800.01 and salario <= 1200.00 :
        novo_salario = salario + ((10 / 100) * salario)
        reajuste = novo_salario - salario 
        percentual = reajuste / (salario / 100)
        print(f"Novo salario: {novo_salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual:.0f} %")

    elif salario >= 1200.01 and salario <= 2000.00 :
        novo_salario = salario + ((7 / 100) * salario)
        reajuste = novo_salario - salario 
        percentual = reajuste / (salario / 100)
        print(f"Novo salario: {novo_salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual:.0f} %")

    elif salario > 2000.00 :
        novo_salario = salario + ((4 / 100) * salario)
        reajuste = novo_salario - salario 
        percentual = reajuste / (salario / 100)
        print(f"Novo salario: {novo_salario:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentual:.0f} %")