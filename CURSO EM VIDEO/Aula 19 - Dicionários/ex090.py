  
"""
 Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

dados_aluno = dict()

dados_aluno['nome'] = input('Nome: ')
dados_aluno['media'] = float(input(f'Media de {dados_aluno["nome"]}: '))
if dados_aluno['media'] >= 7:
    dados_aluno['situacao'] = 'APROVADO!'
elif dados_aluno['media'] >= 6:
    dados_aluno['situacao'] = 'RECUPERAÇÃO'
else:
    dados_aluno['situacao'] = 'REPROVADO!'
print('='*42)
for k, v in dados_aluno.items():
    print(f' - {k} é igual a {v}')