from random import randint
from playsound import playsound
x = randint(0,3)
a = int(input('Diga um numero: '))
if x == a :
    print('Acertou')
    playsound('/home/rubem/Área de Trabalho/CURSO/ARQUIVOS/MP3/Acertou mizeravi.mp3')
else:
    print('Errou')

    playsound('/home/rubem/Área de Trabalho/CURSO/ARQUIVOS/MP3/Faustão - Errou!.mp3')
print('O numero correto é: {}'.format(x))
