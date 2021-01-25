print("""Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço 
antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do 
preço novo (de acordo com a 2ª tabela).
----------------------------------------------------
PREÇO ANTIGO            |   PERCENTUAL DE AUMENTO   

ATÉ R$ 50,00            |       5%
R$ 50,00 - R$ 100,00    |       10%
ACIMA DE R$ 100,00      |       15%
----------------------------------------------------
PREÇO NOVO                         |   MENSAGEM  
                                      
ATÉ R$ 80,00                       |       BARATO
R$ 80,00 - R$ 120,00 (inclusive)   |       NORMAL
R$ 120,00 - R$ 200,00 (inclusive)  |       CARO
ACIMA DE R$ 200,00                 |       MUITO CARO
""")

valor_antigo = float(input('Valor Original: R$ '))

if valor_antigo <= 50:
    valor_final = valor_antigo + (valor_antigo * 0.05)

elif valor_antigo <= 100:
    valor_final = valor_antigo + (valor_antigo * 0.10)

elif valor_antigo > 100:
    valor_final = valor_antigo + (valor_antigo * 0.15)

if valor_final < 80:
    mensagem = "BARATO"
elif valor_final <= 120:
    mensagem = "NORMAL"
elif valor_final <= 200:
    mensagem = "CARO"
else:
    mensagem = "MUITO CARO"
print('*'*27)
print(f'VALOR FINAL R$ {valor_final:.2f} - {mensagem}')
