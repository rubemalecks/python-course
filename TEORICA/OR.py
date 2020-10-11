nome = input('Qual seu nome? ')
print(nome or 'Você não digitou nada')

a = 0       #False
b = None    #False
c = False   #False
d = []      #False
e = {}      #False
f = 22      #True
g = 'rubem' #True

variavel = a or b or c or d or e or f or g
print(variavel) #retorna o 1º TRUE que ele achou segundo a ordem determinada