from math import floor
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = ((n1 + n2)/2)
print('Tirando {:.1f} e {:.1f} a media do Aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Aluno REPROVADO')
if media > 5 and media < 7:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO')
