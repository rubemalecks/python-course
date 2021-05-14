"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários  
são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}
>>> print(type({}))
<class 'dict'>

OBS: Sobre dicionários:
    - Chave e valor são separados por 2 pontos 'chave:valor';
    - Chave pode ser qualquer tipo imutavél, valor pode ser qualquer tipo de dado;
    - Podemos misturar tipos de dados;
-----------------------------------------
# Criação de Dicionários

# Forma 1 (Mais Comum)
>>> paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

>>> print(paises)
>>> print(type(paises))
>>> print(paises['eua'])
-----------------------------------------
# Forma 2 (Menos comum)

>>> paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
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
pais = paises.get('ru', 'Não Encontrei') # pais sempre vai receber um valor

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
# Podemos utilizar qualquer tipo de dado, inclusive (int, float, string, bool, tuplas) 

# Tuplas por exemplo são bastante interessantes como chaves, pois são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (35.7749, 122.4194): 'Escritório em São Paulo'

} 
print(localidades)
print(type(localidades))
-----------------------------------------------
# Adicionando Elementos em Python

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1:

receita['abr'] = 350 # dicionario_existente['new_key'] = valor
print(receita)

# Forma 2:

novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)
---------------------------------------------------
# Atualizando Dados em Um Dicionário

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2 

receita.update({'mai': 500})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados é a mesma
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

----------------------------------------------------
# Removendo dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - MAIS COMUM
ret = receita.pop('mar')
print(ret)
print(receita)
# Precisamos sempre informar a chave, caso não encontre o elemento um KeyError é retornado
# Ao removermos um objeto desta forma(pop) o valor deste é sempre retornado.

# Forma 2

del receita['fev']  # NESTE CASO O VALOR REMOVIDO NÃO É RETORNADO
print(receita)
# Precisamos sempre informar a chave, caso não encontre o elemento um KeyError é retornado
------------------------------------------------------

# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras no qual adicionamos produtos.

'''Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 1:
        - nome;
        - quantidade;
        - preço; 
       
'''
-------------------
# 2 - Poderíamos utilizar uma Lista para isso? Sim.

carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual era o indice de cada informação no produto

------------------------
# Forma 2 - Poderíamos utilizar uma tupla

produto1 = ('Playstation 4', 1 , 2300)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)
-------------------------
# Forma 3 (CORRETA) - DICIONÁRIO
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma facilmente adicionamos ou removemos produtos no carrinho
#  e em cada produto podemos ter a certeza sobre cada informação
-------------------------------------------------------
# Métodos de dicionários
#>>>  dir({}) - ver
-------------------------
d = dict(a=1, b=2, c=3)

print(d)
print(type(d))
------------------
# Limpar o dicionário (Zerar dados) . clear
d.clear()
print(d)
----------------------------

# Copiando um dicionário para outro
EX
d = dict(a=1, b=2, c=3)
---------------

# Forma 1 - Shallow Copy

novo = d.copy() 
print(novo)

novo['d'] = 4

print(d)
print(novo)

------------
EXEMPLO 2 - Shallow Copy

x = dict(a=0, b=1, c=2)

>>> from copy import copy
>>> xc = copy(x)
>>> x == xc     
# True

------------------------------------
# Forma 2 - Deep Copy (cópia profunda)

>>> from copy import deepcopy
>>> xd = deepcopy(x)
>>> x == xd
# True    
------

# POR QUE USAR?

A diferença entre cópia profunda e rasa é relevante apenas para objetos compostos (objetos que contêm 
outros objetos, como listas ou instâncias de classe):
•	Uma cópia rasa constrói um novo objeto composto e então (na medida do possível) insere nele referências 
aos objetos encontrados no original.
•	Uma cópia profunda constrói um novo objeto composto e então, recursivamente, insere nele cópias dos objetos
 encontrados no original.

Frequentemente, existem dois problemas com operações de cópia profunda que não existem com operações de cópia rasa:
•	Objetos recursivos (objetos compostos que, direta ou indiretamente, contêm uma referência a si mesmos) podem 
causar um laço recursivo.
•	Como a cópia profunda copia tudo, ela pode copiar muito, como dados que devem ser compartilhados entre as cópias.

A função deepcopy() evita esses problemas:
•	mantendo um dicionário memo de objetos já copiados durante a passagem de cópia atual; e
•	permitindo que as classes definidas pelo usuário substituam a operação de cópia ou o conjunto de componentes 
copiados.

Este módulo não copia tipos como módulo, método, stack trace (situação da pilha de execução), quadro de empilhamento,
 arquivo, soquete, janela, vetor ou outros tipos 
semelhantes. Ele “copia” funções e classes (rasas e profundamente), devolvendo o objeto original inalterado; isso é
 compatível com a maneira que estes itens são tratados pelo módulo pickle.

Cópias rasas de dicionários podem ser feitas usando dict.copy(), e de listas atribuindo uma fatia de toda a lista, 
por exemplo, lista_copiada = lista_original[:].

# EXEMPLO 2 (usando deepcopy)

>>> from copy import deepcopy
>>> pessoas = ['rubem', 'álecks', 'gabriel', 'angela', ['outros']]
>>> copia_profunda = deepcopy(pessoas)
>>> copia_profunda[4][0] = 'etc'    # ['rubem', 'álecks', 'gabriel', 'angela', ['etc']]
>>> copia_profunda == pessoas
# False

# EXEMPLO 3 (mostrando problema shallow copy)

>>> from copy import copy
>>> pessoas = ['rubem', 'álecks', 'gabriel', 'angela', ['outros']]
>>> copia_rasa = copy(pessoas)
>>> copia_rasa[4][0] = 'etc'    # tanto copia_rasa quanto pessoas são alterados
>>> copia_rasa == pessoas
# True


-----------------------------------------------------------

 # Forma não usual de criação de dicionários


outro = {}.fromkeys('a', 'b') #{}.fromkeys('chave', 'valor')

print(outro)
print(type(outro))'

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'],'desconhecido')
print(usuario)
print(type(usuario)) # 4 key, e 1 unico dados para todos

# O método fromkeys recebe 2 parâmetros: um interável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a essa chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
'''>>> {'t': 'valor', 'e': 'valor', 's': 'valor'}''' # ele não continuou (tes'te') 
# pois em dicionarios não há repetição de chave

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)

Outro Exemplo:

veja = {}.fromkeys('teste', 'valor')
print(veja)
{'t': 'valor', 'e': 'valor', 's': 'valor'}

# Já que dicionarios não podem ter chaves iguais ele só retorna 'test', evitando repetir as mesmas se
chaves (ao usas 't' e 'e') que já eram chaves existentes.
"""
