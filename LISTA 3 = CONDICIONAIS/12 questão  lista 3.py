# Lendo as variaveis hora inicial e hora final

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Determinando a duracao de um jogo com a condicao que a hora inicial é menor que a hora final

if hora_inicial < hora_final :
    horas = hora_final - hora_inicial

# Condicionando os minutos

    if minuto_inicial < minuto_final :
        minutos = minuto_final - minuto_inicial
    elif minuto_inicial > minuto_final :
        horas = horas - 1
        minutos = (60 - minuto_inicial) + minuto_final
    elif minuto_inicial == minuto_inicial :
        minutos = 0

# Imprimindo resultados

    print(f"O JOGO DUROU {horas:.0f} HORA(S) E {minutos:.0f} MINUTO(S)")

# Determinando a duracao de um jogo com a condicao que a hora inicial é maior que a hora final

elif hora_inicial > hora_final :
    horas = (24 - hora_inicial) + hora_final

# Condicionando os minutos

    if minuto_inicial < minuto_final :
        minutos = minuto_final - minuto_inicial
    elif minuto_inicial > minuto_final :
        horas = horas - 1
        minutos = (60 - minuto_inicial) + minuto_final
    elif minuto_inicial == minuto_final :
        minutos = 0

# Imprimindo resultados

    print(f"O JOGO DUROU {horas:.0f} HORA(S) E {minutos:.0f} MINUTO(S)")

# Determinando a duracao de um jogo com a condicao que a hora inicial é igual a hora final

elif hora_inicial == hora_final :

# Condicionando os minutos

    if minuto_inicial < minuto_final :
        minutos = minuto_final - minuto_inicial
        horas = 0
    elif minuto_inicial > minuto_final :
        minutos = (60 - minuto_inicial) + minuto_final
        horas = 23
    elif minuto_inicial == minuto_final :
        horas = 24
        minutos = 0

# Imprimindo resultados

    print (f"O JOGO DUROU {horas:.0f} HORA(S) E {minutos:.0f} MINUTO(S)")
