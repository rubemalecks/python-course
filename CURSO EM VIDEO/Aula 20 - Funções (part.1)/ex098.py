"""
Faça um programa que tenha uma função chamada contador(), que recebe três 
parâmetros:
início, fim e passo e realize a contagem
Seu programa tem que realizar três contagens através da função criada
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada
--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""
from time import sleep

def linha():
    print('=-'*23)
def enunciado(i, f, p):
    linha()
    if p < 0:
        print(f'Contagem de {i} até {f}, de {p*-1} em {p*-1}:')
        sleep(1.0)
    else:
        print(f'Contagem de {i} até {f}, de {p} em {p}:')
        sleep(1.0)
        
def contador(i, f, p):
    if p == 0:
        p = 1
    enunciado(i, f, p)
    if f < i: 
        if p > 0:
            p *= -1
        for x in range(i, f-1, p):
            sleep(0.9)
            print(x,end=' ')
        print('... FIM!!!')
    else:
        if p < 0:
            p *= -1
        for x in range(i, f+1, p):
            sleep(0.9)
            print(x,end=' ')
        print('... FIM!!!')
    linha()

contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
salto = int(input('Salto: '))

contador(inicio, fim, salto)