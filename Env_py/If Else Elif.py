"""
Estruturas Condicionais
"""
#Dizer se um Americano pode beber: 21 anos


idade = 16

if idade < 18:
	print('Menor de idade\nNão pode beber.')
elif idade == 18:
	print('Maior de idade\nMas ainda não pode beber.')
else:
	print('Pode beber')