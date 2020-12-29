'''
DESAFIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
Informe:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos.
'''

t = 0
idade_homem_velho = 0
novinhas = 0
nome_homem_velho = 0
print('*'*17)
for c in range(0,4):
    nome = str(input('Nome: ')).upper()
    sexo = str(input('Sexo (F/M): ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Invalido! Tente Novamente!')
        sexo = str(input('Sexo (F/M): ')).upper()
    idade = int(input('Idade: '))
    t += idade
    print('*'*17)
    if sexo == 'M' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade
    if sexo == 'F' and idade < 20 :
        novinhas += 1
media = t / 4
print('A media de idade é {} anos'.format(media))
print('O homem mais velho é {} com {} anos.'.format(nome_homem_velho, idade_homem_velho))
if novinhas > 1 :
    print('\nTemos {} mulheres com menos de 20 anos.'.format(novinhas))
if novinhas == 0 :
    print('Não temos novinhas')
if novinhas == 1 :
    print('Só temos 1 mulher com menos de 20 anos! '.format(novinhas))
