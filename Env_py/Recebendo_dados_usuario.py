nome = input("qual seu nome?\n")
idade = input("qual sua idade?\n")

#Print feio/antigo 2.x
print("%s tem %s anos" % (nome, idade))


#Print moderno 3.x
print("{0} tem {1} anos".format(nome, idade))

#Print mais moderno 3.7
print(f"Seja bem-vindo {nome}\n" + f"{nome} tem {idade} anos e nasceu em {2020 - int(idade)} ou em {2020 - int(idade) -1}")


#Cast = Converter um tipo de dado para outro. int para string, int para float, etc.
A = 1    # Esta em string
B = int(A)   # Foi convertida para int
C = float(A)  # Foi convertida para float
print(f"veja a diferença:\n {A}\n {B}\n {C}")


#Quando voce quiser um dado em numéro faça o Cast no input
telefone = int(input("Qual seu telefone?"))
print(f'seu telefone é: {telefone}?')