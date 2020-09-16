"""
Módulo Colletions: Deque

É uma lista de alta performance

Te permite manipular (add/pop) items tanto no final quanto no começo, diferente
de uma lista comum.
"""
# Importando
from collections import deque

# Criando deques
deq = deque('geek')
print(deq)
# Adicionando elementos no deque
deq.append('y') # Desse modo padrão o item irá para o final da lista
print(deq)
deq.appendleft('a') # Deque te permite adicionar no inicio da lista
print(deq)