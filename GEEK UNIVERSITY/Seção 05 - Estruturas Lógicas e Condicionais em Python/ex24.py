"""Uma empresa vende o mesmo produto para quatro diferente estados. Cada estado possui
uma taxa diferente de imposto sobre o produto (MG 7%, SP 12%, RJ 15%, MS 8%). Faça um programa
em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço 
final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado 
não for válidado, mostra uma mensagem de erro. """
print('-'*23)
valor_original = float(input('Valor do Produto: '))
estados = {'MG': 7, 'SP': 12, 'RJ': 15, 'MS': 8}
r_estado = ''
while r_estado not in estados:
    r_estado = input('''Estado:
    MG - 7%
    SP - 12%
    RJ - 15%
    MS - 8%
R: ''').upper()
    if r_estado not in estados:
        print('INCORRETO! TENTE NOVAMENTE...')
    print('-'*23)
valor_final = valor_original + (valor_original * (estados[r_estado])/100)
print(f'O valor a ser pago em {r_estado} será R$ {valor_final:.2f} ')
