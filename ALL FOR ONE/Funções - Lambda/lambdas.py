"""Utilizando Lambdas
ex: 
variavel = lambda <entrada> : <retorno>
print(variavel(paramentro_entrada))

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, 
funções anônimas.

# Função em Python

def soma(a,b):
    return a + b

# função em python
def funcao(x):
    return 3 * x + 1

print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' Rubem', 'ÁLECKS '))

# Em funções Python podemos ter nenhuma ou varias entradas. Em lambdas tambem.
amar = lambda: 'Como não amar python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

#n = lambda x1, x2, ..., xn: <expressão>
print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError 

# Outro Exemplo 
#~Ordenação pelo Sobrenome
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 
          'Rubem Álecks', 'Douglas Adams', 'H. G. Wells']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Funções Quadráticas 

# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    #Retorna a funcao f(x) = a*x**2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c
teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

# APLICAÇÕES DE LAMBDA= Filtragem e Aplicação de Dados
"""


def x(sobrenome, nome): return nome.title() + " " + sobrenome.title()

print(x('lopes', 'rubem'))
