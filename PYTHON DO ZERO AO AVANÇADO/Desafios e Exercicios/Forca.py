palavra_secreta = 'rubem'
digitados = []

while True:
    secreto_temp = ''
    dig_letra = input('Digite UMA LETRA: ').lower()
    if not dig_letra.isalpha() or len(dig_letra) > 1 or len(dig_letra) == 0:
        print('-'*23)
        print('POR FAVOR, DIGITE UMA LETRA!!')
        print('-'*23)
        continue
    else:
        digitados.append(dig_letra)
        if dig_letra in palavra_secreta:
            print()
        else:
            digitados.pop()
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitados:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == palavra_secreta:
        print('acabou')
        break