# Lendo as variaveis x, y e z
x = input()
y = input()
z = input()

#Determinando a condição e imprimindo

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro' :
    a = 'aguia'
elif x == 'vertebrado' and y == 'ave' and z == 'onivoro' :
    a = 'pomba'
elif x == 'vertebrado' and y == 'mamifero' and z == 'onivoro' :
    a = 'homem'
elif x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro' :
    a = 'vaca'
elif x == 'invertebrado' and y == 'inseto' and z == 'hematofago' :
    a = 'pulga'
elif x == 'invertebrado' and y == 'inseto' and z == 'herbivoro' :
    a = 'lagarta'
elif x == 'invertebrado' and y == 'anelideo' and z == 'hematofago' :
    a = 'sanguessuga'
elif x == 'invertebrado' and y == 'anelideo' and z == 'onivoro' :
    a = 'minhoca'
print(a)