"""Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro
 em um percurso, calcule o consumo em km/L e escreva uma mensagem de acordo com a 
 tabela abaixo
 
CONSUMO     |   (KM/L)  | MENSAGEM
MENOR QUE   |     8     | VENDA O CARRO!
ENTRE       |   8 E 14  | ECONÔMICO!
MAIOR QUE   |    12     | SUPER ECONÔMICO!


 """

km = float(input('Distância (km): '))
lt = float(input('Gasolina (lt): '))

consumo = km/lt

if consumo < 8:
    print('VENDA O CARRO!')
elif consumo > 8 and consumo < 14:
    print('Econômico!')
elif consumo > 12:
    print('Super Econômico!')
