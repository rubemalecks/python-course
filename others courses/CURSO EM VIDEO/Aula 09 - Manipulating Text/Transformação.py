frase = str('Curso em Video Python')
print(frase.replace('Python', 'Android')) #substitui frase por android
print(frase.upper()) #upper é um metodo() - transforma tudo em maiusculo
print(frase.lower()) #lower()tudo para minusculo
print(frase.capitalize()) #capitalize() td p minusculo e primeira letra p maiusculo
print(frase.title()) #title() - Todas as letras após o espaço maiusculo
frase = '   Aprenda Python  '
print(frase.strip()) #strip() - cria uma lista com separador e excliu os espaços no inicio e final
dividido = frase.sprit()
print(dividido[2][3])
print(frase.rstrip()) #rstrip() - excliu os espaços da direita
print(frase.lstrip()) #lstrip() - excliu os espaços da esquerda
