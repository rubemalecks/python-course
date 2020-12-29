from time import sleep
while True:
    from random import choice
    lista_cpf = [
    "37429948243",  
    "47142947330", 
    "38396123730", 
    "62136277405", 
    "62136277405", 
    "74522626894", 
    "37529143433", 
    "74478543526", 
    "68427484615", 
    "12511183722", 
    "82978579722", 
    "55621928881", 
    "18838164169",]

    #cpf = input('CPF: ')
    cpf = choice(lista_cpf)
    cpf_novo = (cpf[:9])
    cont1 = 1
    soma1, soma2, cont2 = 0, 0,0
    for c in range(len(cpf_novo)):
        soma1 += int(cpf_novo[c]) * cont1
        cont1 += 1
    dig1 = soma1 % 11
    if dig1 == 10:
        dig1 = 0
    cpf_novo = str(cpf_novo) + str(dig1)
    for i in range(len(cpf_novo)):
        soma2 += int(cpf_novo[i]) * cont2
        cont2 += 1
    dig2 = soma2 % 11
    if dig2 == 10:
        dig2 = 0
    cpf_novo = str(cpf_novo) + str(dig2)

    if cpf_novo == cpf:
        print('CPF VALIDO')
    else:
        print('CPF INVÁLIDO')

    print(cpf)
    sleep(0.5)
    if cpf_novo != cpf:
        print('ACHEI UM ERRO!')

    