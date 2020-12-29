from playsound import playsound
print('='*7, 'DETRAN', '='*7)
km = float(input('Velocidade do veiculo: '))
if km > 80 :
    print('Veiculo MULTADO')
    m = (km - 80) * 7
    print('O valor da Multa é : {}'.format(m))
else:
    print('Por enquanto tá tudo tranquilo')
    playsound('/home/rubem/Área de Trabalho/CURSO/ARQUIVOS/MP3/Por enquanto ta tudo tranquilo.mp3')
