palavra_secreta = 'rubem'.upper()
digitados = []
chances = 3
while True:
    
    if chances <= 0:
        print('VOCÊ PERDEU!!')
        break
    secreto_temp = ''


    dig_letra = input('Digite UMA LETRA: ').upper()
    print('-'*23) 
    if not dig_letra.isalpha() or len(dig_letra) > 1 or len(dig_letra) == 0:
        print('POR FAVOR, DIGITE UMA LETRA!!')
        print('-'*23)
        continue
    elif dig_letra in digitados:                        # se repetir uma letra já digitada  
        print('ESTA LETRA JÁ FOI ENCONTRADA, TENTE OUTRA!')
        continue

        
    digitados.append(dig_letra)
    if dig_letra in palavra_secreta:    # se a letra estiver na palavra secreta
        print(f'TEMOS {dig_letra} NA PALAVRA SECRETA!')
        print('-'*23)
    else:
        chances -= 1    

        print('NÃO TEMOS ESSA LETRA NA PALAVRA SECRETA!')                                            
        digitados.pop() 
        print('-'*23)
        if chances >= 1:
            print(f'VOCÊ AINDA TEM {chances} CHANCES!!')
            print('-'*23)


                                                 
    for letra_secreta in palavra_secreta:  
        if letra_secreta in digitados:          # fazer o teste se é == a letra digitada, se for ...
            secreto_temp += letra_secreta       # secreto_temporario recebe a letra quantas vezes for necessario
                    
        else:    
            secreto_temp += '*'                 # caso contrario, concatenar '*'
    
    
    print(f'Palavra Secreta: {secreto_temp}')
    print('-'*23)
    if secreto_temp == palavra_secreta:
        print('VOCÊ GANHOU !!!')
        break
       
                
        