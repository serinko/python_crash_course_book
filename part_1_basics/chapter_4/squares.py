squares = []
	# EMPTY LIST called "squares"
for value in range(1,11):
	# item "value" defined as a variable
	# range 1-11 defined
	# "value" as an item for each in range 1-11
	square = value**2
	# new variable "square" defined as value**
	# We know that "value" is a variable representing items in range(1,11)
	# ** is a Python representation exponents
	# This means that each "square" = "value" in range(1,11) times itself
	squares.append(square)
	# "squares" was the empty list defined in the beginning
	# append adds an item in the end
	# item in append(square) is defined as "square"
	# "square" as a variable was defined above
	# LOOP = all this is happening in the loop due to "if" and "in" functions
	# this adds (append) a value of "square" until the loop runs till the end (number 11)

print(squares)
	# print the list "squares" after the loop
	# each item in the list has a value of "value" in the range(1,11)**itself
	# in range(1,11) we have numbers 1,2,3...10
	# its exponential (**2) value is then the number in the list of "squares"
	
print("\n")

	
	# MORE CONCISELY
	# omit the temporary variale "square"
	# append each new value directly to the list
	
squares = []
for value in range(1,11):
	squares.append(value**3)
	# Each value in the range is immediatelly raised to the second power
	# and directly append to the list
	
print(squares)
