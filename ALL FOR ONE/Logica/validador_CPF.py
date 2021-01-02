cpf = input('CPF: ')
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