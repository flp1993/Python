"""
Módulo Collections -> Default Dict

Ele elimina o 'keyError' gerado numa consulta de uma chave inexistente.
Caso tente acessar uma chave que nao exista, o default dict vai criar
essa chave e atribuir um valor default.

Para isso iremos utilizar o lambda.
Lambda são funções sem nome, que pode ou não receber parametros e
retornar valores.
"""

# Fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)
print('\n')
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro']) # Não existe atualmente essa chave

print(dicionario) # Foi criada a chave 'outro' e foi adicionado o valor padrão do lambda.

