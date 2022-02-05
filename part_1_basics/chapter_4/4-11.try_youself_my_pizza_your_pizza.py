my_pizzas = ['margarita', 'capriciosa', 'quattro formaggi']
friends_pizzas = my_pizzas[:]

my_pizzas.append('frutti di mare')
friends_pizzas.append('fungi')

print("My favorite pizas are:")
for pizza in my_pizzas:
	print(pizza.title())
	
print("\n")

print("My friend's favorite pizas are:")
for pizza in friends_pizzas:
	print(pizza.title())
