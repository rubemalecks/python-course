"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas(entre 0 e 100). A primeira
e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do 
aluno e indicar se o aluno foi aprovado/reporvado. A nota para aprovação deve
 ser igual ou superior a 60 pontos.

"""
while True:
    bim1 = float(input('1º Bimestre: '))
    if bim1 < 0 or bim1 > 100:
        print('Nota Invalida!')
    else:
        break

while True:
    bim2 = float(input('2º Bimestre: '))
    if bim2 < 0 or bim2 > 100:
        print('Nota Invalida!')
    else:
        break

while True:
    bim3 = float(input('3º Bimestre: '))
    if bim3 < 0 or bim3 > 100:
        print('Nota Invalida!')
    else:
        break

mp = ((bim1 * 1) + (bim2 * 1) + (bim3 * 2))/4
print(f'Com {mp} pontos o', end=' ')
print('Aluno está APROVADO!') if mp >= 60 else print('aluno está REPROVADO')
