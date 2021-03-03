print(
    '''
Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a media de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''
)
from time import sleep

boletim_geral = list()

print('=' * 42, '')
print('BOLETIM DE ALUNOS'.center(42))
print('=' * 42, '\n')


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª NOTA: '))
    nota2 = float(input('2ª NOTA: '))
    media = (nota1 + nota2) / 2
    boletim_geral.append([nome, [nota1, nota2], media])
    print('-' * 42)
    continuar = str(input('CONTINUAR?[S/N]: ')).upper()
    print('-' * 42)
    if 'S' not in continuar:
        break
print(f'{"nº":<8}{"ALUNO":<10}{"MÉDIA":>8}')
for indice, dados_aluno in enumerate(boletim_geral):
    print(f'{indice:<8}{dados_aluno[0]:<10}{dados_aluno[2]:>8}')
print('-' * 42)
while True:
    ver_notas = str(input('VER NOTAS? [S/N]: ')).upper()
    if 'S' in ver_notas:
        cod_aluno = int(input('Digite o nº do aluno: '))
        print('-'*42)
        print(
            f'Notas de {boletim_geral[cod_aluno][0]} são {boletim_geral[cod_aluno][1]}'
        )
    
    else:
        print('finalizando...', end='')
        sleep(2)
        break
    print('-'*42)
