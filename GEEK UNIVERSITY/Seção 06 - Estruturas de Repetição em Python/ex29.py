print("""Escreva um programa para calcular o valor da série, 
para 5 termos.\n
S = 0 + 1/2! + 2/4! + 3/6! +...\n""") 

from math import factorial


s, a, b = 0, 1, 2
for c in range(5):
    s += (a/factorial(b)) 
    a+= 1 
    b+= 2
print(f'Resposta: {s}')