'''
ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
'''
print('ALUGUEL DE CARROS')
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilomentros ele percorreu? '))
valor = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {valor:.2f}')



'''
nivel 2 <==
print('ALUGUEL DE CARROS')
modelo = float(input('Escolha o modelo: \n 1) BARRATO \n 2) CARO \n'))
if modelo == 1:
    carro = 150.00
else: carro = 500.00
dias = int(input('Por quantos dias foi alugado: '))
km = float(input('Quantos quilometros rodados: '))
pagar = float((60 * dias) + (km * 0.15) + carro)
print('O total a pagar é de R${:.2f}'.format(pagar))
'''