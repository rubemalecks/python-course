print('''
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. 
A primeira vez deve usar a estrutura de repetição "for", a segunda "while", 
e a terceira "do while".
''')
for c in range(101):
    print(c)

print('-'*23)

x = 0
while x < 100:
    x += 1
    print(x)

print('-'*23)


y = 0
while True:
    y +=1
    print(y)
    if y == 100:
        break

