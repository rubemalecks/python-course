palavra_secreta = 'rrerrr'.upper()
digitados = []
chances = 3
while True:
    print('-'*23)
    if chances < 0:
        print('VOCÊ PERDEU!!')
        break
    secreto_temp = ''


    dig_letra = input('Digite UMA LETRA: ').upper()
    if not dig_letra.isalpha() or len(dig_letra) > 1 or len(dig_letra) == 0:
        print('-'*23)
        print('POR FAVOR, DIGITE UMA LETRA!!')
        print('-'*23)
        continue
    elif dig_letra in digitados:                        # se repetir uma letra já digitada  
        print('ESTA LETRA JÁ FOI ENCONTRADA, TENTE OUTRA!')
        continue


    else:        
        digitados.append(dig_letra)
        if dig_letra in palavra_secreta:    # se a letra estiver na palavra secreta
            for letra_secreta in palavra_secreta:   # para cada letra na palavra
                if letra_secreta in digitados:          # fazer o teste se é == a letra digitada, se for ...
                    secreto_temp += letra_secreta       # secreto_temporario recebe a letra quantas vezes for necessario
                    
                else:
                    secreto_temp += '*'                 # caso contrario, concatenar '*'
            if dig_letra in palavra_secreta:
                print('-'*23)    
                print(f'TEMOS {dig_letra} NA PALAVRA SECRETA!')
        else:
            chances -= 1                                                # cada letra errada -1 chances
            digitados.pop()                                             # e remover da variavel digitados

    print('-'*23)
    print(secreto_temp)


    print('-'*23)
    print(f'VOCÊ TEM {chances} CHANCES!!')
    print('-'*23)


    if secreto_temp == palavra_secreta:
        break
print('-'*23)
print('ACERTOU!')