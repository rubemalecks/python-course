#Calcular desc de produto

valor = float(input('Valor do Produto: '))

desc = valor * 0.12

pagar = valor - desc

print(f'O desconto foi de R${desc:.2f} \nO total a pagar é de R${pagar:.2f}')


