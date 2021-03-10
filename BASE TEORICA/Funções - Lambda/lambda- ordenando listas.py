"""lambda/Funções Ocultas/Ordenando listas em python"""

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

#ESSE:
'''def func(item):
    return item[1] #ITEM[1] ORDENANDO PELO PREÇO [0]É PELO NOME
lista.sort(key=func, reverse=True)'''

#OU

lista.sort(key=lambda item: item [1], reverse=True) # REVERSE = REVERSO MAIOR P/ MENOR

print(lista)
