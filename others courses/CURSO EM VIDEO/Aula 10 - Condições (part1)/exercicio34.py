print('='*22, 'AUMENTO SALARIAL', '='*22)
salario = float(input('Qual o valor do salario: '))
if salario <= 1250 :
    salario_novo = salario + (salario * 0.15)
else:
    salario_novo = salario + (salario * 0.10)
print('O novo salario é R${:.2f}'.format(salario_novo))
