'''9.	Reverso do número. Faça uma função que retorne o reverso 
de um número inteiro informado. Por exemplo: 127 -> 721.'''

def reversor_numerico(x):
    inverso =''
    for c in range(len(x)-1, -1, -1):
        inverso += x[c]
    return inverso
y = input('Digite: ')
print(reversor_numerico(y))