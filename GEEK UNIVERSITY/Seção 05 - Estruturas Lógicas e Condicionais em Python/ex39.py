print('''
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma 
tabela que se considera o salário atual e o tempo de serviço de cada 
funcionário. Os funcionários com menor salário terão um aumento 
proporcionalmente maior do que os funcionários com salário maior, e conforme
o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional
de salário. Faça um programa que leia:

~ o valor do salário atual do funcionário;
~ o tempo de serviço na empresa (anos)

Use a tabela abaixo para calcular o salário reajustado deste funcionário e 
imprima o valor do salário final reajustado, ou uma mensagem caso o 
funcionário não tenha direito a nenhum aumento.

SALÁRIO ATUAL           |       REAJUSTE(%)     |  
ATÉ R$ 500,00           |          25%          |  
ATÉ 1 MIL               |          20%          |  
ATÉ 1,5 MIL             |          15%          |  
ATÉ 2 MIL               |          10%          |  
ACIMA DE 2 MIL          |          SEM AJUSTE   |


TEMP. SERVIÇO           |         BÔNUS         |  
ABAIXO DE 1 ANO         |       SEM BÔNUS       |  
DE 1 A 3 ANOS           |      R$ 100,00        |  
DE 4 A 6 ANOS           |      R$ 200,00        |  
DE 7 A 10 ANOS          |      R$ 300,00        |   
MAIS DE 10 ANOS         |      R$ 500,00        |  
''')


salario = float(input('Salário Atual: R$ '))


if salario <= 500:
    ajuste = 0.25
elif salario <= 1000:
    ajuste = 0.20
elif salario <= 1500:
    ajuste = 0.15
elif salario <= 2000:
    ajuste = 0.10
else:
    ajuste = 0

temp_serv = int(input('Tempo de Serviço: '))

if temp_serv < 1:
    bonus = 0
elif temp_serv <= 3:
    bonus = 100
elif temp_serv <= 6:
    bonus = 200
elif temp_serv <= 10:
    bonus = 300
else: 
    bonus = 500

salario_reajustado = salario + (salario * ajuste) + bonus


print('---'*23)

if ajuste == 0:
    print('sem ajuste salarial')
if bonus == 0:
    print('sem bonus')

print(f'bonus R$ {bonus:.2f} | ajuste R$ {ajuste*salario:.2f}')
print(f'Salário Antigo R$ {salario:.2f}\nSalário Reajustado R$ {salario_reajustado:.2f}')
