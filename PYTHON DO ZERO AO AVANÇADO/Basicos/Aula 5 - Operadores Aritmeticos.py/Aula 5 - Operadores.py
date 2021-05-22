"""

+  # adição
-  # subtração
*  # multiplicação
/  # divisão
// # divisão inteira
** # exponenciação
%  # modulo ou resto da divisão
() # usado para definir a ordem de precedência
"""
x = 10
y = 7
print(f'Adição: x + y = {x + y}')
print(f'Subtração: x - y = {x - y}')
print(f'Multiplicação: x * y = {x * y}')
print(f'Divisão: x / y = {x / y}')
print(f'Divisão Inteira: x // y = {x // y}')

print('Ordem de Precedência, ex:', (x * y - 1))
print('Ordem de Precedência, ex2:', (x * (y - 1)))

# OBS
# + pode ser usado para concatenar str
# * pode ser usado para repetir str