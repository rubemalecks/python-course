print('%'* 77)

print('Tipos de Triângulo')

l1 = float(input('Lado 1 : '))
l2 = float(input('Lado 2 : '))
l3 = float(input('Lado 3 : '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('PODE FORMAR UM TRIANGULO \n')
    if l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2 :
        print('O Triângulo é Isósceles')
    elif l1 == l2 and l2 == l3 :
        print('O Triângulo é Equilátero')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('O Triângulo é Escaleno')
else:
    print('NÃO PODE FORMAR UM TRIANGULO')
print('\n')
print('%'* 77)
