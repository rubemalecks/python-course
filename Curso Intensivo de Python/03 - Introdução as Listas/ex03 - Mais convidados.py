print('''
Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.

• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista.\n''')

convidados = ['Guido van Rossum', 'Mr. Robot', 'Tarantino']

print(f'Atualmente temos 3 convidados {convidados[:3]}\n')

convidados.insert(0,'Ozzy')
convidados.insert(2, 'Fallen')
convidados.append('Barrichello')
print(convidados)

for convite in convidados:
    print('-'*77)
    print(f'{convite}, gostaria de jantar comingo hoje?')
    