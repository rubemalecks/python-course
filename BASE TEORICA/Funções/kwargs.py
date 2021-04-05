""" 
**kwargs
Poderíamos chamar este parámentro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras 
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma 
esses parâmetros extras em um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items(): # 'items' em ingles é = 'itens'
        print(f' A cor favorita de {pessoa} é {cor}')

cores_favoritas(rubem='verde', alecks='azul')


# OBS: Os parâmetros *args e **kwargs não são obrigatórios 
cores_favoritas()
cores_favoritas(geek='navy')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'Você recebeu um cumprimento pythonico Geek!'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza quem vc é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))
# >>> Não tenho certeza quem vc é ...
# >>> Você recebeu um cumprimento pythonico Geek!
# >>> Oi Geek!
# >>> Especial Geek!


# Nas nossas funções podemos ter(NESTA ORDEM);
- Paramentros Obrigatorios;
- *args;
- Paramentros default (não obrigatórios)
- **kwargs

#   exemplo:
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(21, 'Rubinho')
minha_funcao(13, 'Álecks', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Copes', eu='não', vc='vai')
minha_funcao(19,'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmentros na declaração

# função com a ordem correta de parâmentros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1,2,3, sobrenome='University', cargo='Instrutor'))


# Função na ordem incorreta
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]
print(mostra_info(1,2,3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}' 
nomes = {'nome' : 'Rubem', 'sobrenome' : 'lopes'} #dicionario
print(mostra_nomes(**nomes)) # dicionario desempacotado


# Desempacotar com **kwargs(DICIONARIOS)

def soma_multiplos_numeros(a,b,c):
    print(a+b+c)
lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)


dicionario = dict(a=1, b=2, c=3) # OBS! Os nomes da chave em um dicionario devem ser os mesmos da função.
soma_multiplos_numeros(**dicionario)


# OBS! Os nomes da chave em um dicionario devem ser os mesmos da função.
"""

