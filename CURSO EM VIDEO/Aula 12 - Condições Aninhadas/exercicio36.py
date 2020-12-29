print('APROVANDO EMPRESTIMO BANCARIO')
valor_casa = float(input('Valor da casa: '))
salario = float(input('Salario do Comprador: '))
anos = int(input('Pretende pagar em quantos anos? '))
prestacao = valor_casa / (anos *12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {} Reais em {} anos'.format(valor_casa, anos), end=', ')
print('a prestação será de R$ {:.2f} mensais'.format(prestacao))
if prestacao <= minimo:
    print('\033[36;47mEMPRESTIMO APROVADO\033[m')
else:
    print('\033[31;47mEMPRESTIMO NEGADO\033[m')
