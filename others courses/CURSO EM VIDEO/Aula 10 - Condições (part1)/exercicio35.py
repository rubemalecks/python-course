from time import sleep
print('='*22, 'TRIANGULOS', '='*22)
a = float(input('Informe a medida: '))
b = float(input('Informe a medida: '))
c = float(input('Informe a medida: '))
print('='*44)
print('PROCESSANDO...')
sleep(2)
if a < b + c and b < a + c and c < b + a:
    print('PODE FORMAR UM TRIANGULO')
else:
    print('NÃO PODE FORMAR UM TRIANGULO')
print('='*44)
