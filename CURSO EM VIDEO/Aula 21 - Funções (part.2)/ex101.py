""" 
Crie um programa que tenha uma função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, retonando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

# =+ 65 voto opcional

def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc

    if idade >= 16 and idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade > 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade < 16:
        print(f'Com {idade} anos: AINDA NÃO PODE VOTAR!')

nasc = int(input('Em que ano você nasceu? '))
voto(nasc)