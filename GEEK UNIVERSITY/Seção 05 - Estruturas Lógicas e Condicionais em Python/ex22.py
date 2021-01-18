'''Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode 
ou não se aposentar. As condições para aposentadoria são

- Ter pelo menos 65 anos
- Ou ter trabalhado pelo menos 30 anos
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
'''

idade = int(input('Idade: '))
t_contrib = int(input('Tempo de Contribuição: '))

if idade >= 65:
    print('Pode se aposentar!')
elif t_contrib >= 30:
    print('Pode se aposentar!')
elif idade >= 60 and t_contrib >= 25:
    print('Pode se aposentar!')
else:
    print('Ainda não será possível se aposentar... ')
