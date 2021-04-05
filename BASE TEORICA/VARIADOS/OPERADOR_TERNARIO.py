'''Operador Ternário em Python'''
'''Existem várias linguagens que permitem o uso do operador ternário 
(ou terciário), que, em Python, consiste basicamente de uma 
expressão condicional de apenas uma linha. '''
log_user = False
if log_user:
    msg = 'Usuario Logado'
else:
    msg = 'Usuario Precisa logar'
print(msg)

'''com operador ternário:'''

msg = 'Usuário Logado' if log_user else 'Usuario Precisa logar'
print(msg)

#Outro exemplo
idade = 18
de_maior = (idade >=18)
msg = 'pode acessar' if de_maior else 'acesso negado'
print(msg)