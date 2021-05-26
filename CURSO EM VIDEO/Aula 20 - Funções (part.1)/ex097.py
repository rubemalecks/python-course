"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto 
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva("Olá, Mundo!")
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""
def escreva(x):
    print('~'*len(x))
    print(f'{x}')
    print('~'*len(x))

escreva('Olá, Mundo!')
