'''Crie uma função que receba 2 numeros. O primeiro é um valor 
e o segundo um percentual (10%). Retorne (return) o valor do primeiro numero somado
do aumento do percentual do mesmo'''

def perc (x, y):
    r = x + (x * (y/100))
    return r

valor = int(input('Digite um valor: '))
aumento = int(input('Digite o percentual: '))

resultado = perc(valor, aumento)

print(f'R$ {resultado:.2f}')
