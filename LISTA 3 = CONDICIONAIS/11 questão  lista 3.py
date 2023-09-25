# Lendo as variaveis hora inicial e hora final
hora_inicial, hora_final = map(int, input().split())

# Determinado a duração de um jogo e imprimindo resultado 

if hora_inicial < hora_final :
    duracao = hora_final - hora_inicial
    print(f"O JOGO DUROU {duracao:.0f} HORA(S)")

else:

    if hora_inicial > hora_final :
       duracao = (24 - hora_inicial) + hora_final
       print(f"O JOGO DUROU {duracao:.0f} HORA(S)") 
    
    elif hora_inicial == hora_final :
        horas = 24
        print(f"O JOGO DUROU {horas:.0f} HORA(S)")