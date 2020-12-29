

salario_base = float(input('Salario Base: '))
print('='*23)
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
total = salario_base + gratificacao - imposto
print(f'Salario Base: R$ {salario_base:.2f}')
print(f'Gratificação: R$ {gratificacao:.2f}')
print(f'Imposto: R$ {imposto:.2f}')

print(f'Total: R$ {total:.2f}')


