soma = 0
n = input('Digite: ')
q_numeros = len(n)
while q_numeros > 0:
    for c in range(q_numeros):
        q_numeros -= 1
        x = (n[c])
        soma += int(x) 
print(soma)