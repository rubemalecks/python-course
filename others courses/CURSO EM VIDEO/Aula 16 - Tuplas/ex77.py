'''
Exercício Python 077: 
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.     
'''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

print('-'*40)
print(f'{"CONTADOR DE VOGAIS":^40}')
print('-'*40)

for p in palavras: 
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p : 
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            