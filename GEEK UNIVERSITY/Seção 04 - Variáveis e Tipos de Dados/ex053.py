c = float(input('Comprimento: '))
l = float(input('Largura: '))
preço_tela = float(input('Preço: '))

custo = (c*2 + l*2)*preço_tela 

print(f'Para cercar um terreno de {c*l:.2f}², será gasto R${custo:.2f} com telas')
