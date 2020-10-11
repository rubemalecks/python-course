print('='*77)
print('CONVERSOR NUMERARIO')
num = int(input('Digite um numero inteiro: '))
opção = int(input('[1] Binário \n[2] Octal \n[3] Hexadecimal \nOpção: '))
if opção == 1 :
    b = (bin(num))
    b = b[2:]
    print('{} convertido para Binário é {}'.format(num, b))
elif opção == 2 :
    octn = (oct(num))
    octn = octn[2:]
    print('{} convertido para Octal é {}'.format(num, octn))
elif opção == 3 :
    hexn = (hex(num))
    hexn = hexn[2:]
    print('{} convertido para Hexadecimal é {}'.format(num, hexn))
else:
    print('Opção incorreta, tente novamente.')
