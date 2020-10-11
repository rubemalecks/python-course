from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade_atual = ano_atual - ano_nasc
if idade_atual == 18:
    print('Você terá de se alistar este ano!')
elif idade_atual > 18:
    atraso = idade_atual - 18
    print('Já passou da hora de você se alistar!')
    print('Você deveria ter se alistado a {} anos atrás!!'.format(atraso))
elif idade_atual < 18 :
    saldo = 18 - idade_atual
    print('Ainda faltam {} anos para o seu alistamento!'.format(saldo))
    print('Seu alistamento será em {}!'.format(ano_atual + saldo))
