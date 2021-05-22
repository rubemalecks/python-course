""" 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras 
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Nome: ')

if nome.isalpha() and len(nome) > 0:
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) <= 6:
         print('Seu nome é normal.')
    elif len(nome) > 6:
        print('Seu nome é muito grane.')
else:
    print('valor incorreto.')

