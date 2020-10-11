print('Compras no Cartão')
valor_produto = float(input('Valor do produto R$ '))
total = valor_produto
forma_pagamento = int(input('''
1) À VISTA
2) À VISTA CARTÃO
3) 2x CARTÃO
4) 3x OU MAIS NO CARTÃO

FORMA DE PAGAMENTO: '''))
if forma_pagamento == 1 :
    desconto = valor_produto * 0.10
    total = valor_produto - desconto
elif forma_pagamento == 2 :
    desconto = valor_produto * 0.05
    total = valor_produto - desconto
    print('Fica 2x de R$ {}'.format(total/2))
elif forma_pagamento == 3 :
    parcela = valor_produto / 2
    print('2 parcelas de R$ {:.2f}'.format(parcela))
elif forma_pagamento == 4 :
    total = valor_produto + (valor_produto*0.20)
    parcelas = int(input('Quantas Parcelas:'))
    print('Parcelado em {} vezes de R${:.2f} '.format(parcelas, (total/parcelas)))
else:
    print('OPÇÃO INVALIDA TENTE NOVAMENTE!!!')
print('Totalizando R$ {:.2f}'.format(total))
