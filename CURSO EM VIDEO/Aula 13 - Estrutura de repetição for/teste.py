"""
DESAFIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
frase = str(input('Digite a frase: ')).upper().split()
junto = ''.join(frase)
inverso = '' ## começa sem valer "nada"
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
###junto[letra] => junto é uma lista e letra são os itens, a cada interação do for ele complementa o item da lista
## quando a variavel (inverso) recebe o item ele concatena o mesmo ex; a + b + c = abc
print('O contrario de {} é {}'.format(junto, inverso))
if junto == inverso :
    print('TEMOS UM PALINDROMO!')
else:
    print('NÃO É UM PALINDROMO!')
