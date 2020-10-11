
'''ex013: Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento'''

salario = float(input('Qual é o salario do funcionario? R$'))
aumento = salario*0.15
print(f'O novo salario será de R${salario+aumento:.2f}')

