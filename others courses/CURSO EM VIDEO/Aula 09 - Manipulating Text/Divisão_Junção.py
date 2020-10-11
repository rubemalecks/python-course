frase = 'Curso em Video Python'
print(frase.split()) #divide as palavras em lista anulando os espaços
dividido = frase.split()
print((dividido[2][3])) #item 2 letra 3 (split começa de 0 ...)
frase = 'Curso em Video Python'
print('-'.join(frase)) #gera string unica separando letras por '' o item escolhido
