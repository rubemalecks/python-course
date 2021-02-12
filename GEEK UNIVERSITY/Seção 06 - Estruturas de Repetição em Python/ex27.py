print("""Em matemática, o número harmônico designado por H(n) 
define-se como sendo a soma da série harmónica:
h(n)= 1 + 1/2 + 1/3 + 1/4 + ... 1/n""")


n = int(input('Digite um numero: '))
n_hrm = 0
for c in range(1, n+1):
    n_hrm += (1/c)
    d= c
print(f'Resposta: {n_hrm}')
