altura = float(input('ALTURA: '))

sexo = str(input('HOMEM / MULHER: ')).upper()

if sexo[0] == 'H' :
    peso_ideal = (72.7 * altura) - 58
else: 
    peso_ideal = (62.1 * altura) - 44.7
print(f'PESO IDEAL: {peso_ideal:.2f}')
