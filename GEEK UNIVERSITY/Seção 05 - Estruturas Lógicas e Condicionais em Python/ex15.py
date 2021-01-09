""" Usando switch, escreva um programa que leia um inteiro entre 1 e 7 
e imprima o ida da semana correspondente a este numero. Isto é, domingo se 1, 
segunda-feira se 2, e assim por diante"""

dia = int(input("""Escolha um dia da semana: 
\n1 - Domingo \n2 - Segunda-Feira 
3 - Terça-Feira \n4 - Quarta-Feira
5 - Quinta-Feira \n6 - Sexta-Feira
7 - Sábado
--------------
Resposta: """))

print('-'*14)
if dia == 1:
    print('Domingo')

elif dia == 2:
    print('Segunda-Feira')

elif dia == 3:
    print('Terça-Feira')

elif dia == 4:
    print('Quarta-Feira')

elif dia == 5:
    print('Quinta-Feira')

elif dia == 6:
    print('Sexta-Feira')

elif dia == 7:
    print('Sábado')
