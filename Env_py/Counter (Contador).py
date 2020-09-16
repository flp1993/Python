"""
Módulo Collections - Counter
Collections -> High-Performance Container Data type. São coleções tuning
de alta performance.

Counter -> Recebe um parametro iteravel, e cria um objeto counter.
Parece um dicionário, a chave é o parametro recebido e o valor é a
quantidade de ocorrências desse elemento.

"""

# Realizando o import
from collections import Counter
# Podemos usar qualquer iterável: tupla, dict, lista, mapa, etc
lista = [1,1,1,2,2,3,3,3,3,1,1,2,2,4,4,4,5,5,5,5,3,45,45,66,66,43,34]

# utilizando o Counter
    # Exemplo 1
res = Counter(lista)
print(res)
print(type(res))
print('\n')

    # Exemplo 2
print(Counter('Geek University'))

    # Exemplo 3
texto = """The willow it weeps today
A breeze from the distance is calling your name
Unfurl your black wings and wait
Across the horizon it's coming to sweep you away
It's coming to sweep you away

Let the wind carry you home
Blackbird fly away
May you never be broken again

The fragile cannot endure
The wrecked and the jaded a place so impure
The static of this cruel world
Cause some birds to fly long before they've seen their day
Long before they've seen their day

Let the wind carry you home
Blackbird fly away
May you never be broken again

Beyond the suffering you've known
I hope you find your way
May you never be broken again

Ascend may you find no resistance
Know that you made such a difference
All you leave behind will live to the end
The cycle of suffering goes on
But the memories of you stay strong
Someday I too will fly and find you again

Let the wind carry you home
Blackbird fly away
May you never be broken again

Beyond the suffering you've known
I hope you find your way
May you never be broken again
May you never be broken again"""
palavras = texto.split()
res = Counter(palavras)
print(res)
print(Counter(texto))
print('\n')
print(f'As 5 palavras mais comuns na música: {res.most_common(5)}')