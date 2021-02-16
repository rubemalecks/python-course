print("""
Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.
""")
import colorama
colorama.init()
expressao = list(input('Digite a expressão: '))
bateria = 0

for c in expressao:
    if c == '(':
        bateria+=1
    elif c == ')':
        bateria-=1
    if bateria < 0:
        break
if bateria % 2 != 0 or bateria < 0:
    print('\033[7;31;40mEXPRESSÃO INVÁLIDA!!\033[m')
else:
    print('\033[0;32;40mEXPRESSÃO CORRETA!!\033[m')
