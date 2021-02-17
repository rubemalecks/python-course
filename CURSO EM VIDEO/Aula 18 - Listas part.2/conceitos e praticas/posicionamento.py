dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) # Pedro
print(dados[1]) # 25

pessoas = list()
pessoas.append(dados[:]) # Fatiamento Completo (cria uma copia de dados)
print(pessoas) # [['Pedro', 25]]

# LISTA COMPOSTA ~ lista dentro de lista

pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
            
print(pessoas[0][0]) # lista[0] ITEM[0] = PEDRO
print(pessoas[1][0]) # lista[1] ITEM[1] = 19
print(pessoas[2][0]) # lista[2] ITEM[0] = JOÃO
print(pessoas[1])    # lista[1] ['MARIA', 19]