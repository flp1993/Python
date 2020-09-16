"""
Dicionários (Mapas)


São Coleções do tipo Chave/Valor.

Funcionam mais ou menos como o indice nas Listas/Tuplas.
O indice era a chave e o item é o valor.
A diferença é que no Dicionário a chave fica explícita.

	- Dicionários são representados por {}.
	- Cada Chave e valor dentro do dict é separado por ':'  {Chave:Valor, Chave:Valor}.
	- Podemos misturar qualquer tipo de dado.

"""

"""
print(type({})) # Type dict
"""


"""
# Criação de Dicionários:
# Forma 1 (Mais Comum/Recomendada)
paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))


# Forma 2 (Menos Comum)
Cidades = dict(DF='Distrito Federal', GO='Goias', SP='São Paulo')
print(Cidades)
print(type(Cidades))
"""


"""
# Acessando elementos

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai',}

# Acessando via Chave (Se a Chave não existir irá dar erro)
print(paises['br'])
print(paises['eua'])
print(paises['py'])
print('\n')

print('br' in  paises)
print('ru' in  paises) # Chave não existe
print('Estados Unidos' in  paises) # Busca não é feita em Valores.
print('\n')

if 'ru' in paises: # Se a chave 'ru' está em {paises}
    russia = paises['ru'] # {russia} recebe paises com a chave 'ru'
    print(f'{russia}')
else:
	print(f'Ainda não existe esse caraio no dict')
print('\n')

# Acessando via get (Recomendada)
    # Quando não existe a chave ele não dá erro, ele acusa apenas None (vazio, tipo sem tipo)
    # Usamos None para inicializar uma variável que não queremos definir o tipo até receber os dados.
    # None sempre será falso no Python.
print(paises.get('br'))
print(paises.get('ru'))
print('\n')

pais = paises.get('ru', 'Não encontrado') # Podemos defiinir o valor padrão ('Não encontrado') caso não encontre a chave pedida ('ru')
print(f'{pais}')
"""


"""
# Podemos Utilizar qualquer tipo de dado (int, float, str, boolean), inclusive lista, tuplas, dicionários, como chaves de dicionários
localidades = {
	(35.6895, 39.6917): 'Escritório em Tókio',
	(40.7128, 74.0060): 'Escritório em Nova York',
	(37.7749, 12.4194): 'Escritório em São Paulo',
}
	# Tuplas são boas pra serem usadas como Chaves, pois elas são imutáveis
print(localidades)
print(type(localidades))
"""



"""
# Adicionar/Atualizar/Remover elementos num dicionário
    # A forma de adicionar ou atualizar um dicionário é a mesma
    # Assim como nos bancos de dados, NÃO PODEMOS TER CHAVES REPETIDAS.
    # Nunca terá chaves duplicadas, pois se voce add uma chave que já exista, o que vai acontecer é um att.
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
print(type(receita))
print('\n')

    # Forma 1 (Mais Comum) 
receita['abr'] = 350
print(receita)
print(type(receita))
print('\n')

    # Forma 2 (.update())
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)
print(type(receita))
print('\n')

# Atualizando Dados em um dicionário
    # Forma 1
receita['abr'] = 400
print(receita)
print(type(receita))
print('\n')

    # Forma 2
receita.update({'mai': 450})
print(receita)
print(type(receita))
print('\n')


# Removendo dados de um dicionário
    # Forma 1 
receita.pop('mar') # Temos sempre que informar a chave, senão ele vai acusar um error 
print(receita)
print(type(receita))
print('\n')

    # Forma 2 (Mais Comum) 
ret = receita.pop('abr')
print(receita)
print(ret) # Além de retirar o valor também será informado o valor que foi retirado
print(type(receita))
print('\n')

    # Forma 3
del receita['fev'] # Se for um item que não existe, vai dar um 'KeyError'
print(receita)
print(type(receita))
print('\n')
"""


# Casos de aplicação de dicionários
	# E-commerce
'''
Carrinho de compras:
	Produto 1:
		- nome;
		- quantidade;
		- preço;
	Produto 2:
		- nome;
		- quantidade;
		- preço;
'''
# 1 - Podemos utilizar Listas para isso
    # Temos que saber que:
        # Indice 0: é o produto
        # Indice 1: é a quantidade
        # Indice 2: é o preço
'''
carrinho = []

produto1 = ['Ps4', 1, 2300.00]
produto2 = ['GoW 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print('\n')

# 2 - Podemos utilizar Tuplas
    # Temos que saber que:
        # Indice 0: é o produto
        # Indice 1: é a quantidade
        # Indice 2: é o preço
produto3 = ('Ps3',1, 1200.00)
produto4 = ('Gow3',1,50.00)

carrinho2 = (produto3, produto4)
print(carrinho2)
print('\n')


# 3 - Podemos utilizar também um dicionário
	# No dicionário as informações como produto, quantidade e preço já estão bem definidas na visualização
	# Não é preciso lembrar o que cada índice significa.
carrinho3 = []

produto5 = {'nome': 'Ps2', 'quantidade': 1, 'preco': 200.00}
produto6 = {'nome': 'GoW2', 'quantidade': 1, 'preco': 20.00}

carrinho3.append(produto5)
carrinho3.append(produto6)
print(carrinho3)
print('\n')
'''


'''
# Métodos de Dicionários

d = dict(a=1,b=2,c=3)
print(d)
print(type(d))
print('\n')

    # Limpar dicionário (Zerar dados)
d.clear()
print(d)
print('\n')

   # Copiando um dict pra outro dict
       # Forma 1
d = dict(a=1,b=2,c=3)

novo = d.copy() # Deep Copy
print(novo)

novo['d'] = 4
print('\n')
print(d)
print(novo)
print('\n')


        # Forma 2
novo2 = d # Shallow Copy/ Ambos foram alterados
novo2['d'] = 4
print('\n')
print(d)
print(novo2)
print('\n')
'''


'''
# Forma não usual de criação de dicionários
    # .fromkeys()
outro = {}.fromkeys('a', 1)
print(outro)
print(type(outro))
print('\n')

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') # Itens dentro da lista viraram Chaves, o 'desconhecido' virou um valor pra cada Chave
print(usuario)
print(type(usuario))
print('\n')

veja = {}.fromkeys('teste', 'valor') # Str ('teste') são iteráveis, e pra cada valor iterável ele criará uma chave.
print(veja) # Como ele não repete chaves, letras repetidas não serão duplicadas no dict
print(type(veja))
print('\n')

veja2 = {}.fromkeys(range(1,11), 'cu')
print(veja2)
print(type(veja2))
print('\n')
'''



# MAPAS
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

for chave in receita:
	print(chave)
print('\n')

for chave in receita:
	print(receita[chave])
print('\n')

for chave in receita:
	print(f'{chave.title()}: {receita[chave]}')
print('\n')

print(receita.keys()) # Mostrará todas as chaves do dict
print(receita.values()) # Mostrará todas os valores do dict
print('\n')

for chave in receita.keys():
	print(chave)
for valor in receita.values():
	print(valor)
print('\n')

# Desempacotamento de dicts
print(receita.items())

for chave, valor in receita.items():
	print(f'Chave={chave.title()}   Valor=R${float(valor)}')
print('\n')

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
