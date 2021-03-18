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
dados['nasc'] = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho: '))
dados['idade'] = datetime.now().year - dados['nasc']
if dados['carteira'] != 0:
    dados['ano_contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposent'] = dados['idade'] + ((dados['ano_contratacao'] + 35) - datetime.now().year)

    print(dados['aposent'])