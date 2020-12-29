import random
print('SORTEANDO ORDEM DE ALUNOS')
print('Digite o nome dos alunos')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
random.shuffle(alunos) ##a função shuffle não retorna dados
print('Ordem dos alunos:')
print(alunos)
