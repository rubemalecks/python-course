'''Exercício Python 007: 
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

print('CALCULADOR DE MEDIA')
media = 0
for c in range(1,4):
    nota = 0
    nota = float(input(f'Digite sua {c}ª nota: '))
    media += nota / 3
print(f'A sua media no ano foi {media:.2}')

