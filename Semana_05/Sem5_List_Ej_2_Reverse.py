# #2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#     1. Pista: investigue de que otras maneras se puede usar el `range`.


my_string = "Hipopotamo"

for character in range (len(my_string)-1,-1,-1):
	print(my_string[character])

