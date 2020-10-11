number1 = int(input('Digite um numero: '))
number2 = int(input('Digite um numero: '))

if number1 > number2:
    print(f'{number1} é maior que {number2}')
elif number2 > number1:
    print(f'{number2} é maior que {number1}')
else:
    print('NUMEROS IGUAIS')
if number1 != number2:
    print(f'a diferença entre ambos é {number1-number2}')
