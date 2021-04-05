'''DESEMPACOTANDO LISTAS'''
# ele associa os item as variaveis, considerando a ordem
lista = ['Luiz', 'João', 'Maria', 'Rubem']

n1, n2, *restante = lista #*restante recebe o que sobra da lista
print(n1, n2) # vai printar só Luiz e João
print(restante)

'''se quiser pegar o ultimo nome da lista'''

n1, n2, *restante, ultimo_nome = lista #*restante recebe os valores mas o ultimo_nome fica reservado a outra variavel
print(restante, ultimo_nome)


'''se colocar assim:'''
*outra_lista, n1, n2, n3 = lista # n1, n3, n3 vão receber os 3ultimos respectivamente
                                 # e outra_lista recebe os primeiros valores
                                 #cada variavel sem * só recebe 1 valor
"""Se não será usado o restante da variavel"""
"""Use:"""
n1, n2, *_ = lista #O *_ é reconhecido como variavel mas outros programadores entendem melhor que voce não irá usar o restante da lista

lista = [1,2,3]
print(*lista, sep='-') #sep = sepador, *lista = desempacota eles com espaços 
