valor = float(input('Valor: '))
print('='*23)
avista = valor - (valor * 0.10) 
parcelas = valor / 3
comissao = avista * 0.05
comissaop = valor * 0.05

print(f'Valor: R$ {valor:.2f}')
print(f'Valor A Vista: R$ {avista:.2f}')
print(f'Parcelado: 3 x R$ {parcelas:.2f}')
print(f'Comissão Vendedor: R$ {comissao:.2f}')
print(f'Comissão p/ pagamento Parc R$ {comissaop:.2f}')


