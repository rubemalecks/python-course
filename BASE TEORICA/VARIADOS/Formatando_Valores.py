""" Formatando valores com modificações

:s - String - se quiser mudar o type(variavel) na impressão
:d - inteiro
:f - flutuante
:.(NUMERO)f - Quantidade de casa decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro

"""
nome = 'rubem'
num_1 = 1
num_2 = 1150
print(f'{num_2:0>10}') #numero vai ter 10 casas e o zer0 vai complementar a esquerda
print(f'{num_2:0<10}') #numero vai ter 10 casas e o zer0 vai complementar a direita
print(f'{num_1:.2f}') # printa o num_1 como um float

print(f'{nome:^20}') 
print(f'{nome:*^20}') #nome alinhado e complementa os 20 caracteres com o * - podemos escolher o caractere de preenchimento
print(f'{nome:^23}')

