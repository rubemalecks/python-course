valor_h = float(input('Valor Hora: '))
horas = float(input('Horas trabalhadas: '))

total = (valor_h * horas) 
totalx = total + (total*0.10)
print(f'Valor a Pagar: R$ {totalx:.2f}')
