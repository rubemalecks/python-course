'''Crie uma função1 que recebe uma função2 como paremetro 
e retorne o valor da função2 executada.'''

def func1():
    return 'hello world!'
def func2(funcao):
    return funcao()

exe = func2(func1)
print(exe)