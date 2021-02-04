print(''' 
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação 
de acordo com a tabela abaixo:


        IMC         |   Classificação
       < 18,5       |   Abaixo do Peso
    18,6 - 24,9     |   Saudável
    25,0 - 29,9     |   Peso em excesso
    30,0 - 34,9     |   Obesidade Grau I
    35,0 - 39,9     |   Obesidade Grau II(severa)
        >=40        |   Obesidade Grau III(mórbida)

''')

peso = float(input('PESO: '))
altura = float(input('ALTURA: '))

imc = peso / altura**2
if imc <= 18.5:
    classificacao = 'Abaixo do Peso'
elif imc <= 24.9:
    classificacao = 'Saudável'
elif imc <= 29.9:
    classificacao = 'Peso em Excesso'
elif imc <= 34.9:
    classificacao = 'Obesidade Grau I'
elif imc <= 39.9:
    classificacao = 'Obesidade Grau II(severa)'
else:
    classificacao = 'Obesidade Grau III(mórbida)'

print(f'O IMC é = {imc:.2f} - {classificacao}')