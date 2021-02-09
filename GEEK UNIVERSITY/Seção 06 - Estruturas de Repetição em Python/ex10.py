print('Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares.')


soma = 0
print('-'*77)
for c in range(101):
    if c % 2 == 0:
        soma+= c

print(f'Resposta: {soma}')
print('-'*77)