print('''
Faça um algoritmo utilizando o comando while que mostre uma contagem 
regressiva na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem 
'FIM' após a contagem. ''')

from time import sleep
contagem = 10
while contagem >= 0:
    sleep(1)
    print(contagem, end='...')
    contagem-= 1
print('FIM')