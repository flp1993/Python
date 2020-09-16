"""
Listas
    Funcionam como vetores/matrizes (arrays), com a diferença
de serem DINÂMICOS e poderem colocar QUALQUER tipo de dado.

- Array:
    Possuam tamanho e tipo de dado fixo. Exemplos:
        Array int, tamanho 5 (5 valores).
        Array str, tamanho 50 (50 valores).

    No python ele é DINÂMICO, não define tamanho. O limite é
o tamanho da memória da sua máquina.
    Além disso, as listas não possuem tipo de dado fixo.

As listas em python são representadas por: [].

"""

"""
lista1 = [0,1,2,3,4,5,6,7,8,9,10]

lista2 = list(range(99))

lista3 = []

lista4 = ['G','e','e','k',' ','U','n','i','v','e','r','s','e']

lista5 = list('Geek University')

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)



# Podemos checar se determinado valor está na lista
num = int(input('Pesquise o número na lista: '))
if num in lista2:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')
"""
"""
             # Agora vamos manipular as listas

# .sort() ordena a lista
lista6 = [1,56,54,44,10,2,3,4,68,5,869,456,8,1,2,31,1,1,1,1,1]
lista6.sort()
lista5.sort()
print(lista6)
print(lista5)


# Podemos encontrar o número de ocorrências de um valor na lista
print(lista6.count(1))
print(lista5.count('e'))


# Adicionar elementos na lista .append()
# Só dá pra adicionar 1 elemento por vez e vai para o final da lista
# Podemos adicionar até lista dentro da lista
lista7 = ['luis']
print(lista7)
lista7.append('Felipe')
print(lista7)
lista7.append(['07 de dezembro','1993'])
print(lista7)


# É possivel adicionar item informando a posição do índice
lista6.insert(3,'valor .insert')
print(lista6)


# .extend() só aceita + de 1 valor na adição
# Podemos juntar listas usando .extend() ou "+"
lista7.extend(['Rodrigues','Albuquerque'])
print(lista7)
lista6.extend(lista4)
print(lista6)


# Podemos também reverter uma lista
lista1.reverse()
print(lista1)
print(lista6[::-1])


# Copiando listas
lista9 = lista2.copy()


# Contando elementos da lista
print(len(lista6))


# Removendo o ultimo elemento de uma lista .pop() ou pelo índice
print(lista5)
lista5.pop()
print(lista5)
lista5.pop(3) # Elemento na posição 3
print(lista5)


# Vamos converter string para lista
curso = 'Programação em Python essencial'
print(curso)
curso = curso.split() # Por padrão usará " " como separador
print(curso)
curso2 = 'Programação,em,Python,essencial'
curso2 = curso2.split(',') # Agora o separador é ','
print(curso2)


# Convertendo listas em String

curso3 = ''.join(lista4) # o que tiver nas aspas é o separador
print(curso3)
lista10 = ['Luis','Felipe']
nome1 = '$'.join(lista10)
print(nome1)


         # Iterando sobre listas
lista1.reverse()
soma = ''
for elemento in lista4:
    soma = soma + elemento
print(f'A soma dos elementos é: {soma}')

# Vamos iterar usando while e for
carrinho = []
produto = ''

while produto != 'sair':
    print("Selecione o produto ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)


# Listas que recebe variáveis
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1,num2,num3,num4,num5]
print(numeros)


# Indexação de forma inversa
 #          0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
 #         -4         -3       -2       -1

for indice in enumerate(cores):
    print(indice[0], end= ' = ')
    print(indice[1])
print(f'-4 = {cores[-4]}')
print(f'-3 = {cores[-3]}')
print(f'-2 = {cores[-2]}')
print(f'-1 = {cores[-1]}')
'''


         # Métodos não tão importantes mas ÚTEIS

'''
# Encontrar o índice de um elemento na lista

produtos = ['Ps4', 'iPhone', 'Galaxy', 'RX 580' ]
numeros2 = [5, 6, 7, 5, 8, 9, 10]
    # Qual indice está a RX 580?
print(f'O Produto RX 580 está no índice: {produtos.index("RX 580")}')
    # Qual indice está a Ps4?
print(f'O Produto Ps4 está no índice: {produtos.index("Ps4")}')
    # Caso não existe o produto na lista será apresentado um erro
#print(f'O Produto Knk está no índice: {produtos.index("Knk")}')


# Fazendo busca dentro de um range:
print(f'O índice é: {numeros2.index(5, 2)}') # Procurar o "5" a partir do item 2
print(f'O índice é: {numeros2.index(8, 3, 5)}') # "5" entre o item 3 e 5

# Slice de lista com parâmetro 'inicio'
    # Lista[inicio:fim:passo]
lista20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista a partir do item 3: {lista20[3:]}')
print(f'Lista do item 3 ao 7: {lista20[3:8]}') # 8 pq o 8º não é incluso
print(f'Lista do inicio ao 8: {lista20[:9]}')
print(f'Lista inteira de 2 em 2: {lista20[::2]}')
print(f'Lista inteira de 3 em 3: {lista20[::3]}')
print(f'Lista inteira de 4 em 4: {lista20[::4]}')
'''

'''
# Invertendo valores em uma lista
nomes = ['Geek', 'University']
print(f'Indice 0 é: "{nomes[0]}" e no indice 1 é: "{nomes[1]}"')

nomes[0], nomes[1] = nomes[1], nomes[0]
print(f'Indice 0 agora é: "{nomes[0]}" e no indice 1 agora é: "{nomes[1]}"\nA lista foi invertida')
print(f'Mas isso poderia ser feito usando o método ".reverse()"')
'''

'''
# Soma, Valor Máximo, Valor Mínimo, Tamanho nas listas
    # Só serve se for lista com valores inteiros ou flutuantes
lista = [1, 2, 3, 4, 5, 6, 2.0, 656.0, 99, 1.5, 5.2, 7.7, 545, 1215.9]
print(sum(lista)) # Soma toda a lista
print(max(lista)) # Valor Máximo da lista
print(min(lista)) # Valor Mínimo da lista
print(len(lista)) # Mostra o tamanho da lista
'''

'''
# Transformar Listas em Tuplas
lista = [1, 2, 3, 4, 5, 6, 2.0, 656.0, 99, 1.5, 5.2, 7.7, 545, 1215.9]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(f'\n{tupla}')
print(type(tupla))
'''

'''
# Desempacotamento de Listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(f'{num1}\n{num2}\n{num3}')
    # Tem que ter o mesmo número de variáveis e itens
lista2 = [1, 2, 3, 4]
num4, num5, num6 = lista2 # 4 itens e 3 var, vai dar erro
print(f'{num4}\n{num5}\n{num6}')
'''

'''
# Copiando uma lista para outra (Shallow copy e Deep copy)
ExtremamenteCobradoEmEmpregos = True
    # Forma 1
print(f'                        EXEMPLO DE DEEP COPY:')
lista = [1, 2, 3, 4, 5, 6]
print(f'Lista1:{lista}')

novalista = lista.copy() # Deep copy faz um clone independente
print(f'Copia da Lista1 (Nova Lista): {novalista}')
novalista.append(7)
print(f'Lista1 após adição na Nova lista:{lista}')
print(f'Nova lista após adição do "7": {novalista}')

print(f'\n\n                    EXEMPLO DE SHALLOW COPY:')
lista2 = [1, 2, 3, 4, 5, 6]
print(f'Lista2:{lista2}')
novalista2 = lista2 # Shallow faz um apontamento, são DEPENDENTES
print(f'Copia da Lista2 (Nova Lista2): {novalista2}')
novalista2.append('simulação na nova lista2')
print(f'\nUma adição foi feita em "Nova lista2": {novalista2}')
print(f'Nada aconteceu com a "lista2": {lista2}')
print(f'\nMas se o contrário for feito acontecerá...')
lista2.append('Adição somente em "lista2"')
print(f'\nUma adição foi feita em "lista2": {lista2}')
print(f'"Nova Lista2" foi afetada também nessa adição:\n{novalista2}')
'''