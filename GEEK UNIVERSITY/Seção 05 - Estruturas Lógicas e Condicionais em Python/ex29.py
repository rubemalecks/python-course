'''Faça uma prova de matemática para crianças que estão aprendendo a somar
números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100,
e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os números
aleatórios. Peça a resposta. Faça 5 perguntas ao aluno, e mostre para ele as
perguntas e as respostas corretas, além de quantas vezes o aluno acertou.'''

from random import randint
print('-'*23)
gab = []

print('PROVA DE MATEMATICA')
certas, erradas = 0, 0
print('-'*23)
for c in range(5):
    x = randint(1, 100)
    y = randint(1, 100)
    r = int(input(f'{x} + {y} = '))
    quest = (f'{x} + {y} = {x+y}')

    if r == (x + y):
        print('ACERTOU')
        certas += 1
    else:
        print('errou')
        erradas += 1

    gab.append(quest)
print('-'*23)
print(f'Você acertou {certas} perguntas')
print(f'Você errou {erradas} perguntas')

print('-'*23)
print('GABARITO: ')
cont_gab = 0
for resp in gab:
    cont_gab += 1
    print(cont_gab, ')', resp)
