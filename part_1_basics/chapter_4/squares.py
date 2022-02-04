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
	squares.append(value**)
	# Each value in the range is immediatelly raised to the second power
	# and directly append to the list
	
print(squares)
print("\n")

	# Both versions are good
	# Sometimes adding a temporary variable makes it easier to understand the code
	# sometimes it is better to be as concise
	# aprroah this question according the priority of 
	# 1) Make sure you understand your code well
	# 2) Look for simplification and efficiency when you review the code

	# LIST COMPREHENSIONS
	# this is the shortest way the previous list can be witten like
	# this way is often presented by other programmers
squares = [value**2 for value in range (1,11)]
	# begin with descriptive name of the list "squares"
	# define the expression of he value = "value**2"
	# a for loopto generate the numbers into the expression
	#the for loop is for value in the given range
	# which feeds the value through the expression value**2
	# No colon is used in the end
print(squares)
	
	# It takes practie to make your own comprehensions
	# when the lines become repetative - consider writing your own comprehensions
