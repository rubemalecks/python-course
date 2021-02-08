print('''
Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não
poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.\n''')

# PART. 1 
# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não
# poderá comparecer.
convidados = ['Guido van Rossum', 'Elliot Aldersen', 'Tarantino']

print(f'Olá, {convidados[0]}, gostaria de jantar comigo hoje?')
print(f'Olá, {convidados[1]}, gostaria de jantar comigo hoje?')
print(f'Olá, {convidados[2]}, gostaria de jantar comigo hoje?')

nao_veio =  convidados.pop(1)

print(f'{nao_veio} não pode vir hoje')


# PART. 2
# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.
convidados.insert(1, 'Mr. Robot')


# PART. 3 
# Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.

print(f'Olá, {convidados[0]}, gostaria de jantar comigo hoje?')
print(f'Olá, {convidados[1]}, gostaria de jantar comigo hoje?')
print(f'Olá, {convidados[2]}, gostaria de jantar comigo hoje?')