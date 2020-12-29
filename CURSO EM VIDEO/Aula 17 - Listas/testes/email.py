
from time import sleep

print('FACEBOOK.COM')
email = ''
senha = ''
email_0 = input('Digite Seu Email: ')
senha_0 = input('Digite Sua Senha: ')

print('Aguarde', end='')
sleep(0.3)
for c in range(0,3):
    print(('.'),end='')
    sleep(1)
print()
print('#'*29)
print('Bem Vindo Ao Facebook')
while email != email_0 or senha != senha_0:
    email = input('Digite Seu Email: ')
    senha = input('Digite Sua Senha: ')
    if email != email_0 or senha != senha_0:
        print('Dados incorretos!!')
if email == email_0 and senha == senha_0:
    print('LOGIN EFETUADO')
    print('[BEM VINDO AO FACEBOOK!!]')
