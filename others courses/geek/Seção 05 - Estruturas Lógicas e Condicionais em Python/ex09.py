salario = float(input('SALARIO: R$ '))
prestacao = float(input('PRESTAÇÃO: R$ '))

parcela = (prestacao / salario) * 100

if parcela >= 20 :
    print('EMPRESTIMO NEGADO!!')
else: 
    print('EMPRESTIMO CONCEDIDO!!')
