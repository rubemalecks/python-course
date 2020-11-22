'''Crie uma função1 que recebe uma função2 como paremetro 
e retorne o valor da função2 executada.'''

def func1(func2):
    return func2()

def func2():
    return 'Rubinho'

print(func2())