"""
Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: 
o primeiro que indique o número a calcular e o outro chamado show, que será 
um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial. Deve haver docstring na função criada.


"""


def fatorial(x, show=False):
    """[Fatorial]

    Args:
        x ([int]): [número a ser calculado]
        show (bool, optional): 
            [True] mostra a conta,  
            [False] não mostra a conta.

    Returns:
        [int]: [Fatorial de x]
    """
    r = 1
    for c in range(x, 0, -1): 
        r *= c
        if show:
            if c == 1:
                print('1 =', end=' ')
                continue
            print(f'{c}', end=' x ')
    return r
help(fatorial)
print(fatorial(5))
