from random import randint
print('''

BEM VINDO NOOB!!!

''')

letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'Ç', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç')


# op_menu = int(input('''
# 0 - só letras
# 1 - numeros
# 2 - letras e numeros
# '''))

senha_gerada = list()
q_digitos = int(input('Quantos Digitos: '))

for c in range(q_digitos):

    l_or_num = randint(0, 1)
    if l_or_num == 0:
        dig_aleatorio = randint(0, len(letras))
        senha_gerada.append(letras[dig_aleatorio])
    else:
        dig_aleatorio = randint(0, 9)
        senha_gerada.append(dig_aleatorio)
# print(senha_gerada)
senha_gerada = str(senha_gerada)
senha_gerada = senha_gerada.strip().replace("'", "").replace(
    "]", "").replace("[", "").replace(",", "").strip()
print(senha_gerada)
