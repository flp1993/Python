"""
Ranges

- Precisamos conhecer o loop for pra usar o ranges.
- Precisamos conhecer o range pra trabalhar melhor com loop for

Ranges sao usados pra gerar sequencia numericas de maneira especificada

Formas gerais:

Forma 1
range(valor_de_parada)
Obs: valor_de_parada não inclusive, sempre 1 anterior

Forma 2
range(valor_de_inicio,valor_de_parada)
Obs: valor_de_parada não inclusive, sempre 1 anterior

Forma 3
range(valor_de_inicio, valor_de_parada, passo)
Obs: Passo especificado pelo usuário. Pode contar de 2 em 2 por exemplo

Forma 4 (Igual a Forma 3, mas inverso)
range(valor_de_inicio, valor_de_parada, passo)




"""

# Forma 1
soma = 0
aux = 0
for num in range(2): # Valor máximo é 10, mas printa até 9
    soma = int(input("Valor pra soma:"))
    aux = aux + soma
    print(f'{aux}\n')

# Forma 2
for num in range(2,10):
    print(num)

# Forma 3
for num in range(1,100,20):
    print(num)

# Forma 4
for num in range(10,-1,-2): # Contagem regressiva
    print(num)

