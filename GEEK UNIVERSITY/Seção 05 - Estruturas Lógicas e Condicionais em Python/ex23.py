"""Determine se um ano lido é bissexto. Sendo que um ano é bissexto se for divisivel 
por 400 ou se for divisivel por 4 e não for divisivel por 100. Por exemplo: 1988, 1999
1996"""

ano = int(input('Digite um ano: '))
if ano % 400 == 0:
    print(f'{ano} é bissexto')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
