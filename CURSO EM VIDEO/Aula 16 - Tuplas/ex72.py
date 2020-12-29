'''
Exercício Python 072:
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
 e mostrá-lo por extenso.
'''

extenso  = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze','dezesseis','dezessete', 'dezoito', 'dezenove','vinte')
continuar = 'S'
while continuar == 'S':    
    while True:
        print('-'*40)
        print(f'{"Número por Extenso":^40}'.upper())
        print('-'*40)
        num = int(input('Escolha um numero entre 0 - 20: '))
        if 0 <= num <= 20 :
            break
    print(f'Por extenso: {extenso[num]}')
    print('-'*40)
    continuar = str(input('Quer Continuar? (S/N) ')).upper()
if continuar == 'S':
    print('FIM DO PROGRAMA...')
    
