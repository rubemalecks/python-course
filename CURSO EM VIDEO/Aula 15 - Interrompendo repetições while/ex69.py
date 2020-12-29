"""
DESAFIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
print()
print('PROGRAMA DE CADASTRO')

cont_homens = 0
maior_idade = 0
menos_20 = 0

print()
while True :
    continuar = ' '
    sexo = ' '
    idade = int(input('IDADE: '))
    while sexo not in 'FM' :
        sexo = str(input('SEXO(F/M): ')).upper().strip()[0]
    print()
    if idade >= 18 :
        maior_idade += 1
    if sexo == 'F' and idade <= 20 :
        menos_20 += 1
    if sexo == 'M' :
        cont_homens += 1
    while continuar not in 'SN' :
        continuar = str(input('Quer continuar?(S/N) ')).upper().strip()[0]
    print()
  
    if continuar == 'N':
        break
    else:
        print('CADASTRO')
print(f' Foram cadastradas {maior_idade} pessoas com +18 anos')
print(f' Foram cadastrados {cont_homens} homens')
print(f' Foram cadastradas {menos_20} mulheres com menos de 20 anos')
