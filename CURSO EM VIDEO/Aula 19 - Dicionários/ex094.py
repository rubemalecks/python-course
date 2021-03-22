"""
Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""
cadastro = {}
lista = []
resp = ''
mulheres = []
soma_idade = int()
acima_media = list()
print()
while True:    
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [F/M]: ')).upper()
    cadastro['idade'] = int(input('Idade: '))
    soma_idade += cadastro["idade"]
    if cadastro["sexo"] == 'F':
        mulheres.append(cadastro["nome"])
    lista.append(cadastro.copy())
    print('='*42)
    resp = str(input('Continuar[S/N]: ')).upper()
    print('='*42)
    if 'S' not in resp:
        break
media_idade = soma_idade/len(lista)
for key, value in enumerate(lista):
    if value['idade'] > media_idade and value['sexo'] == 'F':
        acima_media.append(value["nome"])
        acima_media.append(value["idade"])

print(f'A) Ao todo foram cadastradas {len(lista)} pessoas')
print(f'B) A média de idade é {media_idade:.1f}')
print(f'C) Mulheres cadastradas: {mulheres}')
print(f'D) Acima da media foram: {acima_media}')