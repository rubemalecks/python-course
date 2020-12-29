frase = 'Curso em Video Python'
print(len(frase)) #comprimento da frase
print(frase.count('o'))#Contagem de quantas vezes existe a letra 'o'
print(frase.count('o',0,13)) #Contagem + fatiamento do 0 ao 13
print(frase.find('deo')) #procurar onde começou
print(frase.find('Android')) # retorna-1 pois não existe
print('Curso' in frase)#se existe a palavra curso em frase
