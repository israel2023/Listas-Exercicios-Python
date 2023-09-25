# Ler dados do funcionario e quantidade de vendas
nome_do_vendedor=input()
salario_fixo=float(input())
total_de_vendas=float(input())
# Calculo do valor total recebido pelo funcionario do mes
TOTAL=salario_fixo+((15*total_de_vendas)/100)
# Imprimir valor recebido pelo funcionario
print(f"TOTAL = R$ {TOTAL:.2f}")
