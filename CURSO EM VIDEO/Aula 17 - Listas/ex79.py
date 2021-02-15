print("""
Exercício Python 079: 
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os 
valores únicos digitados, em ordem crescente. 
""")

lista_valores = []
continuar = 'S'
while continuar == 'S':
    v = int(input('Digite um valor: '))
    if v not  in lista_valores:
        lista_valores.append(v)
        print('-'*23)
        print('adicionado com sucesso...')
    else:
        print('[valor duplicado!!]')
    continuar = str(input('Quer continuar? [s/n]: ')).upper()
    print('-'*23)
lista_valores.sort()
print(f'Você Digitou: {lista_valores}')
