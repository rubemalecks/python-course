print("""Faça um algoritmo que encontre o primeiro múltiplo de 11, 13
 ou 17, após um numero dado.\n""")

num = int(input('Informe um número: '))
mult_n = num

while True:
    mult_n+=1
    if mult_n % 11 == 0:
        vlr = 11
        break

    if mult_n % 13 == 0:
        vlr = 13
        break

    if mult_n % 17 == 0:
        vlr = 17
        break
print(f"O multiplo mais proximo é {mult_n}\nPois {mult_n}/{vlr}{' = 0'}")