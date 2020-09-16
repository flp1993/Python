"""
Módulo Colletions: Named Tuple

É um Tupla que te permite dar um nome à ela própria e aos items também.

"""
# Importando
from collections import namedtuple

# Vamos definir o nome e os parâmetros.
    # Forma 1 - Declaração
cachorro = namedtuple('cachorro', 'idade raça nome')
    # Forma 2
cachorro = namedtuple('cachorro', 'idade, raça, nome') # Foi adicionada uma vírgula
    # Forma
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])


# Utilizando

dogs = cachorro(idade=5, raça='shihtzu', nome='Cacau')
print(dogs)

# Acessando os dados
    # Forma 1
print(dogs[2]) # Nome
print(dogs[1]) # Raça
print(dogs[0]) # Idade
print('\n')

    # Forma 2
print(dogs.nome)
print(dogs.raça)
print(dogs.idade)

