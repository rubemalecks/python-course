from datetime import date
ano_atual = date.today().year
maiores_idade = 0
menores_idade = 0
for c in range(0,7):
    n = str(input('Informe seu nome: '))
    a = int(input('Informe o ano de nascimento: '))
    idade = ano_atual - a
    if idade < 18 :
        menores_idade += 1
    else:
        maiores_idade += 1
print('No total temos {} maiores de idade e {} menores de idade'.format(maiores_idade, menores_idade))
