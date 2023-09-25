# Lendo a variavel
idade=int(input())
# Calculando dias em anos, meses e dias
anos=idade//365
mes=(idade%365)//30
dia=((idade%365)%30)
# Imprimindo resultado
print(anos,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")
