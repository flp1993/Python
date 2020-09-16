"""
Loop for

Loop: Estruturas de repetição
For: É uma dessas estruturas

    Estrutura em Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre
valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 8, 9]
- Range
    numeros = range(1, 10)
"""

# Retire as aspas pra rodar o código:

"""
nome = 'Geek University'
lista = [1, 3, 5, 8, 9]
numeros = range(1, 10) #Temos que transformas em lista

# Exemplo 1 For (Iterando em uma String)

for letra in nome:
    print(letra)

# Exemplo 2 For (Iterando em uma lista)

for numero in lista:
    print(numero)

# Exemplo 3 For (Iterando sobre um range)

for numero in range(1, 11):
    print(numero)
"""
"""
nome = 'Geek University'
lista = [1, 3, 5, 8, 9]
numeros = range(1, 10)

# Exemplo for com enumerate():
for i, v in enumerate(nome):
    print(nome[i])
# Enumerate:[0,"G"] [1,"e"] [2,"e"] [3,"k"] [4," "] [5,"U"]

# Exemplo
for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
# "_" é usado para descartar um item, no caso o indice.

# Vamos printar o indice e sua respectiva String
for indice in enumerate(nome):
    print(indice)
    print(indice[0]) # Tras somente o indice
    print(indice[1]) # Tras somente as letras
"""
"""
qtd = int(input('Quantas vezes esse loop vai rodar?'))
soma = 0

for n in range(1,qtd+1):
    num = int(input(f'Informe o valor {n}/{qtd} : '))
    soma = soma + num
print(f'A soma é {soma}')


"""
"""
nome = 'Geek University'

for letra in nome:
    print(letra, end = '')
    # Por padrão o end é um '\n', se voce colocar ' ' ele não vai pular linhas
"""
nome = 'Geek'
for num in range(1,10):
    print(f'{nome*num}')
nome = 'Geek University'
lista = [1, 3, 5, 8, 9]
numeros = range(1, 10)

for indice, letra in enumerate(nome):
    print(letra)