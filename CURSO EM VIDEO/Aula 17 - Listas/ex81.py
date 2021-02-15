print("""Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
""")
lista_numeros = []
continuar = 'S'

while continuar == 'S':
    numero = int(input('Digite um número: '))
    lista_numeros.append(numero)
    continuar = str(input('Continuar [S/N]: ')).upper()
    print('-'*29)
    if continuar not in 'S':
        break
print(f'Foram digitados {len(lista_numeros)} valores')
lista_numeros.sort(reverse=True)
print(f'Os valores foram {lista_numeros}')
if 5 in lista_numeros:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
