'''8.	Faça uma função que informe a quantidade de dígitos de
 um determinado número inteiro informado.'''


def cont_dig(x):
    return len(x)
n = str(int(input('Digite: ')))
print(f'{n} tem {cont_dig(n)} digitos')
