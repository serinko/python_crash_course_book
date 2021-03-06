# This is how lists look like, using [] brackets.
bicycles = ['trek','cannondale', 'redline', 'specialized']

# To print an item, use an index number of the item
print(bicycles[0])
print("\n")

# Methods learnt in chapter_2 can be used. ie .title() to keep the grammar
print(bicycles[2].title())
print("\n")

# A syntax -1, returns the last item from the list
print(bicycles[-1])
print("\n")

# Any [-x] can be used to return an index counted - from the end.
print(bicycles[-3])
print("\n")

# Any value or concatenation can be used, just as a variable
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
