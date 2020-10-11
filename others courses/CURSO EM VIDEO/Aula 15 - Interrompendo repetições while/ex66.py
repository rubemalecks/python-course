"""
DESAFIO 066: Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
numero = soma = cont = 0
print('*'*23)
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma = soma+numero
    cont += 1
print('*'*23)
print(f'A soma é igual a {soma}')
print(f'Foram digitados {cont} numeros ')
