print('~'* 77)
print('Índice de Massa Corporal')
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2)

if imc < 18.5 :
    print('ABAIXO DO PESO')
if imc >= 18.5 and imc < 25 :
    print('PESO IDEAL')
if imc >= 25 and imc < 30 :
    print('SOBREPESO')
if imc >= 30 and imc <= 40 :
    print('OBESIDADE')
if imc > 40 :
    print('OBESIDADE MORBIDA')

print('IMC: {:.1f}'.format(imc))
print('~'* 77)
