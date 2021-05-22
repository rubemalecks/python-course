"""
* Criar variáveis para nome(str), idade (int)
* Altura (float) e peso (float) de uma pessoas
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa(baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com chaves)
"""

nome = str('Rubem')
idade = int(22)
altura = float(1.74)
peso = float(74)
ano_atual = int(2021)
imc = peso/altura**2

print(f'- {nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'- O imc de {nome} é {imc:.2f}')
print(f'- {nome} nasceu em {ano_atual - idade}')

print('"asas"')