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
-----------------------------------------
# Criação de Dicionários

# Forma 1 (Mais Comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))
print(paises['eua'])
-----------------------------------------
# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
------------------------------------------

# Acessando Elementos:


# Forma 1 - Acessando via Chave, parecido com a forma de lista/tupla
# só que dicionarios usam chaves inves de indices 
print(paises['br'])
# Caso tentemos fazer um acesso de uma chave inexistente teremos um 'KeyError'

# Forma 2 - Acessando via get - FORMA RECOMENDADA 
print(paises.get('br'))
print(paises.get('ru')) # caso não encontre a chave retorna None, sem gerar KeyError

# Recomenda-se usar sempre o .get 


# Outro Mod da forma 2:
pais = paises.get('ru', 'Não Escontrei') # pais sempre vai receber um valor

print(pais)
# Podemos definir um valor padrão caso não encontremos o objeto com a chave informada
---------------------------------------------
# Consultando Chaves em dicionario: 

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # False, ele busca key e não valor

if 'ru' in paises:
    russia = paises ['ru']
    
---------------------------------------------
# Podemos utilizar qualquer tipo de dado inclusive (int, float, string, bool) 
# até listas e tuplas, como chaves

# Tuplas por exemplo são bastante interessantes como chaves, pois são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (35.7749, 122.4194): 'Escritório em São Paulo'

}
print(localidades)
print(type(localidades))
-----------------------------------------------
"""
# Adicionando Elementos em Python

receita = {
    'jan': 100, 'fev': 120, 'mar': 300
}
print(receita)
print(type(receita))

# Forma 1:

receita['abr'] = 350
# dicionario_existente['new_key'] = valor

print(receita)

# Forma 2:

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)
