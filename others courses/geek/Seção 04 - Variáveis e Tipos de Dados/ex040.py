#diaria - imposto de resda
diaria = 30

dias = int(input('Dias trabalhados: '))
bruto = dias * diaria

liq = bruto - (bruto*0.08)

print(f'O valor bruto é {bruto:.2f} \nO Desc é R${bruto*0.08:.2f}\nO Liquido é R${liq:.2f}')
