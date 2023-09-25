# Lendo as variavéis
n1, n2, n3, n4 = map(float,input().split())
# Calculando a média do aluno
media=(n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1 )/10
# Imprindo resultado da média
print(f"Media: {media:.1f}")
# Definindo qual a condição desse aluno e imprimindo se ele foi aprovado ou reprovado
if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0 :
    print("Aluno reprovado.")

elif media>= 5.0  <= 6.9 :

    print("Aluno em exame.")
    nota_do_exame = float(input())
    if nota_do_exame > 4.9 :
        print(f"Nota do exame: {nota_do_exame:.1f}")
        media_final = (media + nota_do_exame)/2
    
    if media_final >= 5.0 :
        print("Aluno aprovado.")  
        print(f"Media final: {media_final:.1f}")
    else:
        print("Aluno reprovado.")  


