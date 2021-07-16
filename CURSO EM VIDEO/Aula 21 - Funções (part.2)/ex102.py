"""
Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: 
o primeiro que indique o número a calcular e o outro chamado show, que será 
um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial. Deve haver docstring na função criada.


"""


def fatorial(x, show=False):
    """[Fatorial]

    Args:
        x ([int]): [recebe um numero inteiro]
        show (bool, optional): 
            [True] mostra a conta,  
            [False] deixa ela oculta.

    Returns:
        [int]: [Fatorial de x]
    """
    r = 1
    for c in range(x, 0, -1): 
        r *= c
        if r > 1 and show == True:
            if c == 1:
                print('1 =', end=' ')
                continue
            print(f'{c}', end=' x ')
    return r
help(fatorial)
print(fatorial(5,True))
