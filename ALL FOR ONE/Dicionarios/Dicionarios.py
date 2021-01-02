"""
Dicionários

OBS: Em algumas linguagens de programação, os dicioários Python 
são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}
print(type({}))
>>> <class 'dict'>

OBS: Sobre dicionários:
    - Chave e valor são separados por 2 pontos 'chave:valor';
    - Tanto chave qaunto valor podem ser qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de Dicionários

# Forma 1 (Mais Comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))
print(paises['eua'])
"""
# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
