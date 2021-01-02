'''Crie uma função1 que recebe uma função2 como parametro e 
retorne o valor da função 2 executada. 
Faça a função1 executar duas funções que recebam um 
numero diferente de argumentos'''


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def saudacao(nome, saudacaof):
    return f'{saudacaof} {nome}'


executando = mestre(saudacao, 'Rubem', saudacaof='Bom dia!')
print(executando)
