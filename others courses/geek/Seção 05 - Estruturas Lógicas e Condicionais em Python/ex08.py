nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
if nota1 or nota2 > 10 :
    print('VALOR INVÁLIDO')
elif nota1 or nota2 < 0 : 
    print('VALOR INVÁLIDO')
else:
    print(f'A MEDIA = {media}')
