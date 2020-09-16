"""
PEP8 - PYTHON ENHANCEMENT PROPOSAL

São propostas de melhorias para a linguagem Python
The Zen of Python
Import this

A ideia da pep8 é que possamos escrever codigos Python de forma Pythonica
"""
"""
[1] - Utilize a Camel Case para nomes de classes; 
    Inicial Maiúscula
    Não Usar underline 
"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass

"""
[2] - Utilize nomes em minúsculo, separados por underline para funções e variáveis;
"""
def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5

"""
[3] - Utilize 4 espaços para identação!
    Não é recomendado usar TAB
"""

if 'a' in 'banana':
    print('tem')


""""
[4] - Linhas em Branco
    Separar funções e classes com 2 linhas em branco;
    Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports devem ser feitos em linhas separadas
    Se for imports de um mesmo pacote recomenda-se o uso de chaves;
    Devem ser colocados no topo do documento;
"""

import pandas
import matplotlib
from types import{
    StringType,
    ListType,
    SetType
}
"""
[6] - Não coloque espaços em expressões, instruções e declaração de variáveis
"""
"""
[7] - Termine sempre uma expressão com uma nova linha
    Utilize uma linha em branco;
"""
