"""
Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os 
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário 
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Carteira de Trabalho: (0 não tem): '))

if dados['carteira'] != 0:

    dados['ano_contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contratacao'] + 35) - datetime.now().year)
print('='*42)
for c, v in (dados.items()):
    print(f'~ {c} tem o valor {v}')