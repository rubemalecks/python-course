'''Dados 3 valores, A, B, C, verificar se eles podem ser valores dos 
lado de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou isócele, 
considerando os seguintes conceitos

- O comprimento de cada lado de um triângulo é menor do que a soma dos outros lados
- Equilátero é o triângulo que tem 3 lados iguais
- Isósceles é o triângulo que tem o comprimento de 2 lados iguais
- Escaleno é o triângulo que tem 3 lados diferentes
   '''
while True:
    lado_a = float(input('Lado A: '))
    lado_b = float(input('Lado B: '))
    lado_c = float(input('Lado C: '))

    if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
        break
    else:
        print('Não há como formar um triângulo.\nTente Novamente...')
if lado_a == lado_b == lado_c:
    print('É um triângulo EQUILÁTERO')
elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
    print('É um triângulo ISÓSCELES')
elif lado_a != lado_b != lado_c:
    print('É um triângulo ESCALENO')
    
