print('''
Faça um programa que leia \033[0;32;40mnome e peso de várias pessoas\033[m
guardando tudo em uma \033[0;32;40mlista\033[m. No final mostre:

(A) Quantas pessoas foram cadastradas.
(B) Uma listagem com as pessoas mais pesadas.
(C) Uma listagem com as pessoas mais leves.
''')
continuar = 'S'
c_pessoas = 0
maior = menor = 0
entrada_dados = list()
tratamento_dados = list()
while True:
    print('-='*42)
    entrada_dados.append(str(input('Nome: ')).upper())
    entrada_dados.append(float(input('Peso: ')))
    c_pessoas += 1
    if len(tratamento_dados) == 0: # PARA A 1º ENTRADA: MENOR = MAIOR
        p_maior = p_menor = entrada_dados[0]
        maior = menor = entrada_dados[1]
    elif entrada_dados[1] == menor:
        p_menor+= '...' + str(entrada_dados[0]) # DE QUEM É O MENOR VALOR
    elif entrada_dados[1] == maior:
        p_maior+= '...' + str(entrada_dados[0]) # DE QUEM É O MAIOR VALOR

    if entrada_dados[1] > maior: # TRATAMENTO DO MAIOR VALOR
        p_maior = entrada_dados[0] # DE QUEM É O MAIOR VALOR
        maior = entrada_dados[1]
    if entrada_dados[1] < menor: # TRATAMENTO DO MENOR VALOR
        p_menor = entrada_dados[0] # DE QUEM É O MENOR VALOR
        menor = entrada_dados[1]
    
    tratamento_dados.append(entrada_dados[:]) # TRATAMENTO  RECEBE A ENTRADA DE DADOS
    entrada_dados.clear() # LIMPAR ENTRADA DE DADOS PARA O PROX TRATAMENTO

    continuar = str(input('Continuar[S/N]: ')).upper()
    if 'S' not in continuar:
        break
print('-='*42)
print(f'Ao todo foram cadastradas {c_pessoas} pessoas.')
print(f'O maior peso foi {maior:.1f}kg de {p_maior}.')
print(f'O menor peso foi {menor:.1f}kg de {p_menor}.')