"""
Tuplas (tuple)

São bastantes parecidas com listas

Existem basicamente duas diferenças básicas:
	1. Tuplas são representadas por "( )"
	2. As tuplas são imutáveis, ao se criar uma tupla ela nao muda.
		Toda operação em uma tupla gera uma nova tupla.

# Métodos de adição e remoção não existe, pois elas são imutáveis.
"""



"""
								CUIDADOS
# CUIDADO 1: Tuplas são representadas por () mas podem ser criadas sem os ()
tupla1 = (1,2,3,6,5) 
tupla2 = 1,2,3,5,4,6,8,7
print(type(tupla1))
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4) # Isso não é uma tupla
print(type(tupla3))
tupla4 = (4,) # Isso é uma tupla
tupla5 = 5,
print(type(tupla4))
print(type(tupla5))
	# Tuplas sao definidas não pelo uso do parenteses, mas pela virgula
"""


"""
tupla = tuple(range(11))
print(tupla)
"""


"""
tupla = ('Geek University','Programação em Python')

escola, curso = tupla

print(escola)
print(curso)
"""



"""
tupla = (1,2,3,4)
print(len(tupla))
"""

"""
# Concatenação de tuplas
tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9,10)
print(tupla1)
print(tupla2)
print(tupla1 + tupla2) # Foram unidas, porém não foram alteradas
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Agora os valores foram sobreescritos
print(tupla1)
"""

"""
# Iterando sobre uma tupla
tupla = (1,2,3,4)

for n in tupla:
    print(n)

for indice,valor in enumerate(tupla):
    print(f'Indice {indice}: {valor}')
"""
"""
# Contando elementos
tupla = ('a','b','c','d','e','a','b')
print(tupla.count('b')) # Vai contar quantos "b's" existem ali.
"""

"""
# Dicas de utilização:
# Devemos usar tuplas SEMPRE QUE os dados contídos ali não precisarem de modificação
# Exemplo 1:
meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
"""



"""
# Por quê utilizar tuplas?
  # Processamento mais rápido que Listas.
  # Deixam o código mais seguro, pois sao imutaveis.
"""


# Copiando uma tupla para outra
tupla = (1,3,5)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (7,8,9)
nova = nova + outra
print(nova)
