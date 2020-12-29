"""
DESAFIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
print()
print('*'* 27)
print('TABUADA')
while True :
    print('*'* 27)
    numero = int(input('Você quer ver a tabuada de que valor? '))
    if numero <= 0 :
        print('PROGRAMA ENCERRADO!')
        break
    for c in range(1,11) :
        print(f'{numero} x {c:^2} = {numero*c:^2}')

