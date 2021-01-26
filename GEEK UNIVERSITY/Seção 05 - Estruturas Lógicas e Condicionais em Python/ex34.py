print('''Leia a nota e o número de faltas de um aluno, e escreva seu 
conceito. De acordo com a tabela abaixo, quando o aluno tem mais de 20
 faltas ocorre uma redução de conceito.
 
NOTA            |       CONCEITO (ATÉ 20 FALTAS)      |       CONCEITO (MAIS DE 20 FALTAS)
 
9.0 ATÉ 10.0    |                   A                 |             B
7.5 ATÉ 8.9     |                   B                 |             C
5.0 ATÉ 7.4     |                   C                 |             D
4.0 ATÉ 4.9     |                   D                 |             E
  0 ATÉ 3.9     |                   E                 |             E 
 ''')

nota = float(input('NOTA: '))
faltas = int(input('FALTAS: '))


if nota < 3.9:
    conceito = 'E'

elif nota <= 4.9:
    if faltas <= 20:
        conceito = 'D'
    else:
        conceito = 'E'

elif nota <= 7.4:
    if faltas <= 20:
        conceito = 'C'
    else:
        conceito = 'D'

elif nota <= 8.9:
    if faltas <= 20:
        conceito = 'B'
    else:
        conceito = 'C'
elif nota <= 10:
    if faltas <= 20:
        conceito = 'A'
    else:
        conceito = 'B'
print(f'O conceito final do aluno foi {conceito}')