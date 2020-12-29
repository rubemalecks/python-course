nome = str(input('Digite seu nome completo: ')).strip()
print('Nome: {}'.format(nome))
nome1 = nome.split()
print('Primeiro nome: {}'.format(nome1[0]))
print('Último nome: {}'.format(nome1[-1]))
#PRECISEI CRIAR UMA NOVA VARIAVEL (NOME1) POIS SPLIT NÃO ALTERA A VARAVEL ORIGINAL
