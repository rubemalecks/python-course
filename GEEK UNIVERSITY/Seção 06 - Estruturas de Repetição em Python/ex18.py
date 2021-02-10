print('''Escreva um algoritmo que leia certa quantidade de números 
e imprima o maior valor deles e quantas vezes o maior número foi lido.
A quantidade de números a seres lidos deve ser fornecida pela usuário.\n''')

maior_numero = int()
q_numeros = int(input('Quantidade de números: ')) # ler x quantidade de numeros
lista_numeros = []
print('-'*23)
for c in range(q_numeros):
    x = int(input('Digite um número: '))
    if len(lista_numeros) == 0:
        maior_numero = x
    lista_numeros.append(x)
    if x > maior_numero:
        maior_numero = x
print('-'*23)
# maior valor e qtd de vezes que o mesmo foi lido
print(f'O maior valor foi {maior_numero}.')
print(f'{maior_numero} foi encontrado {lista_numeros.count(maior_numero)} vezes.')