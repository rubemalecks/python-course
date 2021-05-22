nome = 'rubem'
idade = 21
altura = 1.70
peso = 70
imc = peso/altura**2
# print(nome, 'tem', idade, 'anos e seu imc é', peso/(altura**2))

# com f'strings :
# print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')


'''USANDO O FORMAT'''
# print('O {nome} tem {idade} anos e seu imc é '.format(nome, idade))

# podemos deixar vazia
# print('O {} tem {} anos e seu imc é {}'.format(nome, idade, imc))
# indicar os indices
# print('O {0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
# tambem podemos usar paramentros nomeados
# print('O {n} tem {i} anos e seu imc é {im:.2f}'.format(n = nome, i = idade, im = imc))
