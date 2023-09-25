# Lendo a variavel mes

mes = int(input())

# se o mes não estiver entre 1 e 12, ele não existe

if mes !=1 and mes !=2 and mes !=3 and mes !=4 and mes !=5 and mes !=6 and mes !=7 and mes !=8 and mes !=9 and mes !=10 and mes !=11 and mes !=12 :
    print("Nao existe esse mes")

# Determinado a condição que se encaxe no mes que foi pedido e imprindo o resultado na tela

else:

    if mes == 1 :
        print("January")
    elif mes == 2 :
        print("February")
    elif mes == 3 :
        print("March")
    elif mes == 4 :
        print("April")
    elif mes == 5 :
        print("May")
    elif mes == 6 :
        print("June")
    elif mes == 7 :
        print("July")
    elif mes == 8 :
        print("August")
    elif mes == 9 :
        print("September")
    elif mes == 10 :
        print("October")
    elif mes == 11 :
        print("November")
    elif mes == 12 :
        print("December")