""" A nota final de um estudante é calculada a partir de 3 notas
 atribuidas entre o intervalo de 0 a 10, respectivamente, a um trabalho
  de laboratório, uma avaliação semestral, e a um e a um exame final. 
  A média das 3 notas mencionadas anteriormente obedece aos pesos: 

  - Trabalho de Laborátorio: 2
  - Avaliação Semestral 3
  - Exame Final 5
  
  De acordo com o resultado, mostre na tela se o aluno está 
  reprovado (entre 0 a 2,9)
  recuperação (entre 3 a 4,9) 
  acima = aprovado

  Faça todas as verificações necessárias 
  """
print('=:'*20)
while True:
    laboratorio = float(input('Trabalho de Laborátorio: '))
    if laboratorio < 0 or laboratorio > 10:
        print('valor_inválido!')
    else:
        break

while True:
    avaliacao_semestral = float(input('Avaliação Semestral: '))
    if avaliacao_semestral < 0 or avaliacao_semestral > 10:
        print('valor_inválido!')
    else:
        break

while True:
    exame_final = float(input('Exame Final: '))
    if exame_final < 0 or exame_final > 10:
        print('valor_inválido!')
    else:
        break
print('-'*20)
media = ((laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5)) / 10
if media <= 2.9:
    print(f'REPROVADO - {media} pontos')
elif media >= 3 and media <= 4.9:
    print(f'EM RECUPERAÇÃO - {media} pontos')
else:
    print(f'APROVADO - {media} pontos')

print(
    f'NOTAS : Trabalho de Laborátorio[{laboratorio}], avaliação semestral[{avaliacao_semestral}], Exame Final[{exame_final}]')
print('=:'*20)
