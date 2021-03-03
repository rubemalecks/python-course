teste = list()
teste.append('Gustavo')
teste.append(40)
#print(teste) # ['Gustavo', 40] - Estrutura Composta
print('-'*33)

galera = list()
galera.append(teste[:]) # [:] ELE APPEND UMA CÓPIA DE TESTE
# galera.append(teste[:]) '''FORMA ERRADA'''
#print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # galera.append(teste[:]) '''FORMA ERRADA'''
print(galera)