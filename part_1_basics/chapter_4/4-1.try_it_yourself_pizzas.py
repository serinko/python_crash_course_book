pizzas = ['margarita', 'capriciosa', 'quattro formaggi']
for pizza in pizzas:
	print("I really the taste of " + pizza.title() + " pizza.\n")
	# prints a sentence with each pizza
	
message = str(pizzas[0].title()) + ", " + str(pizzas[1].title()) + " and " \
    + str(pizzas[2].title()) + " are my favourite three kinds of pizza.\n"
	# uses pizzas[index] as a refference
print(message)
	# both variable messgae and print function outside of the loop
	# It will be printed only once in the end of the program
