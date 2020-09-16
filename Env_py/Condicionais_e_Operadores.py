"""
Estruturas Condicionais
"""
# Dizer se um Americano pode beber: 21 anos


idade = 16

if idade < 18:
    print('Menor de idade\nNão pode beber.')
elif idade == 18:
    print('Maior de idade\nMas ainda não pode beber.')
else:
    print('Pode beber')

"""
Estruturas Logicas: and, or, not, is
    Operadores Unários:
        not;
    Operadores Binários: 
        and, or, is
        
and -> Ambos valores precisam ser True 
or  -> Um ou outro valor precisa ser True
not -> Inverte o valor booleano

"""

ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo!')
else:
    print('Ative sua conta ou faça login!')
