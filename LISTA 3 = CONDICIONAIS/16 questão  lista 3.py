# Lendo a variavel salario

salario = float(input())

# Calculando e imprimido o imposto quando o salario está entre 0 e 2000

if salario >= 0 and salario <= 2000.00 :
    print("Isento")

else:

# Calculando e imprimido o imposto quando o salario está entre 2000.01 e 3000.00 

    if salario >= 2000.01 and salario <= 3000.00 :
        salario = salario - 2000
        imposto = (8 / 100) * salario 
        print(f"R$ {imposto:.2f}")
    
# Calculando e imprimido o imposto quando o salario está entre 3000.01 e 4500.00 

    elif salario >= 3000.01 and salario <= 4500.00 :
        salario = salario - 2000
        salario_2 = salario - 1000
        imposto = (8 / 100) * 1000 
        imposto_2 = salario_2 * ( 18 / 100)
        imposto_3 = imposto + imposto_2
        print(f"R$ {imposto_3:.2f}")

# Calculando e imprimido o imposto quando o salario é maior que 4500.00 

    elif salario > 4500.00 :
        imposto = (8 / 100) * 1000
        imposto_2 = (18 / 100) * 1500
        salario = salario - 4500
        imposto_3 = imposto + imposto_2 + salario * (28/100)
        print(f"R$ {imposto_3:.2f}")