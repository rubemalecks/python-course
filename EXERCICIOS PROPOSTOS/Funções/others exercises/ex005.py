'''5.	Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.'''



def somaImposto(taxaImposto, custo):
    #calc imposto
    custo_final = custo + (custo*(taxaImposto/100))
    return custo_final

taxaImposto = int(input('Valor da Taxa: '))
custo = int(input('Valor do Produto: '))

print(somaImposto(taxaImposto, custo))
