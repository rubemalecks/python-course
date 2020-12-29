print('#'*77)
print('CAMPEONATO DE NATAÇÃO')
from datetime import date
atual = date.today().year
nome = str(input('Nome: '))
nascimento = int(input('Idade: '))
idade = atual - nascimento
if idade <= 9 :
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('Participante: {}'.format(nome))
print('Categoria: {}'.format(categoria))
