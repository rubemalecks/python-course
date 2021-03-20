print("""
Exercício Python 080: 
Crie um programa onde o usuário possa digitar cinco nes numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
)

lista = []
for c in range(5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado no final...')
    elif valor < lista[0]:
        lista.insert(0, valor)
        print('Valor adicionado no inicio...')
    else:
        for index, v in enumerate(lista):
            if valor <= v:
                lista.insert(index, valor)
                print('Valor adicionado no meio...')
                break       
print(f'Os valores digitados foram {lista}')