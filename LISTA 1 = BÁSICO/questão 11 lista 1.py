
cod_1, qtda_1, vlr_1=input().split()
cod_2, qtda_2, vlr_2=input().split()
qtda_1=int(qtda_1)
vlr_1=float(vlr_1)
qtda_2=int(qtda_2)
vlr_2=float(vlr_2)
total=qtda_1*vlr_1+qtda_2*vlr_2
print(f" VALOR A PAGAR: R$ {total:.2f}")
