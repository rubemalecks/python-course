print('''Faça um programa que receba 2 números. Calcule e mostre:
~ a soma dos números pares desse intervalos de números, incluindo
os números digitados; 
~ a multiplicação dos números ímpares desse intervalo, incluindo 
os digitados;\n''')
while True:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    if n1 < n2:
        break
    else:
        print('O 1º Número deve ser menor que o 2º Número!!')

soma_par = 0
mult_impar = 1
for c in range(n1, n2+1):
    if c % 2 == 0:
        soma_par += c
    else:
        mult_impar *= c

print(f'A soma dos pares é {soma_par}')
print(f'A multiplicação dos ímpares é {mult_impar}')
