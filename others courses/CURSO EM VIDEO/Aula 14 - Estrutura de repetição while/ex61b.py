"""
DESAFIO 061: Progressão Aritmética v2.0
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""
from time import sleep
term = int(input('Primeiro termo: '))
rate = int(input('Razão: '))
tenth_term = term + (10 - 1) * rate 
term_add = 0
choice = 1
print(term, end=' → ')
while term < tenth_term :
    term += rate
    if term == tenth_term:
        print(term)
    else:
        print(term,end=' -> ')
while choice == 1 :
    sleep(0.5)
    choice = int(input("""Quer mostrar mais termos ? \033[1;41m[0] NÃO \033[m/\033[0;44m [1] SIM \033[m \nResposta: """))
    if choice == 1 :
        term_add = int(input('Quantos ? '))
        print('Processando...')
        sleep(2)
        tenth_term += rate * term_add
        while term < tenth_term:
            term += rate
            if term < tenth_term:
                print(term, end=' -> ')
            else:
                print(term)
if choice == 0 :
    print('Saindo ...  ')
    sleep(1.5)


