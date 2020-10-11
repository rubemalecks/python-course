"""
DESAFIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
tipo = ' '
while True :
    jogador = int(input('Escolha um numero inteiro: '))
    computador = randint(1,5)
    resultado = (jogador + computador) % 2
    if resultado == 0 :
        tipo_resultado = 'PAR' 
    else: 
        tipo_resultado = 'IMPAR'
    while tipo not in 'PI':
        tipo = str(input('Escolha -> PAR OU IMPAR (P/I): '))
    print(f'Você escolheu {jogador} e o PC {computador}', end=',')
    print(f' O numero =>{resultado} é {tipo_resultado}')
   
