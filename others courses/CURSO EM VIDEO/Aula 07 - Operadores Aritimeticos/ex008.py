'''Exercício Python 008: 
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
 

x = float(input('Digite um valor em metros: '))
km = x / 1000
hc = x /100
dc = x / 10
dm = x * 10
c = x * 100
m = x * 1000

print(f'{x} metros equivalem a {km:.3f} kilometros')
print(f'{x} metros equivalem a {hc:.2f} hectometros')
print(f'{x} metros equivalem a {dc:.2f} decametros')
print(f'{x} metros equivalem a {dm:.2f} decimetros')
print(f'{x} metros equivalem a {c:.2f} centimetros')
print(f'{x} metros equivalem a {m:.2f} milimetros')
