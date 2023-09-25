# Lendo as variaveis

_,diaInicio = input().split()
hi, mi, si = map(int, input().split(" : "))
_,diaFinal =  input().split()
hf, mf, sf = map(int, input().split(" : ")) 

diaInicio = int(diaInicio)
diaFinal = int(diaFinal)

# Transformando hora inicial e somando com minuto inicial

mi += hi * 60

# Transformando hora final e somando com minuto final

mf += hf * 60

# Transformando minuto inicial e somando com segundo inicial

si += mi * 60

# Transformando minuto final e somando com segundo final

sf += mf * 60

# Calculando dia 

dia = diaFinal - diaInicio

if sf < si :
    sf += 24 * 60 * 60
    dia -= 1

# Duracao em segundos

segundos = sf - si

# Transformando segundos em minutos

duracao_minutos = segundos // 60

# Transformando minutos em segundos

segundos -= duracao_minutos * 60

# Transformando minutos em horas

duracao_horas = duracao_minutos // 60

# Transformando horas em minutos

duracao_minutos -= duracao_horas * 60

# Imprimindo resultados

print(f"{dia:.0f} dia(s)")
print(f"{duracao_horas:.0f} hora(s)")
print(f"{duracao_minutos:.0f} minuto(s)")
print(f"{segundos:.0f} segundo(s)")

































