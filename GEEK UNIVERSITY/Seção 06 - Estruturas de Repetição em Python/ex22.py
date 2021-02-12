print('''Escreva um programa completo que permita a qualquer aluno
 introduzir, pelo teclado, uma sequência  arbitrária de notas 
 (válidas no intervalo de 10 a 20) e mostre na tela, como resultado, 
 a correspondente média aritmética. O número de notas com que o aluno
 pretenda efetuar o cálculo não será fornecido ao programa, o qual 
 terminará quando for introduzido um valor que não seja válido como 
 nota de aprovação\n''')

x, n, soma = 0, 0, 0
while True:
    x = float(input('Digite a nota: '))
    if x >= 10 and x <= 20:
        soma += x
        n+= 1
    else:
        break
media_arit = soma/n
print(f'A média aritmética é {media_arit:.2f}.')

