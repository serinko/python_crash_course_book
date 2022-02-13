user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# items() function returns a list key-value pairs
# the list assigns the pair to the provided variables in the statement
# any name for the variables can be chosen
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"Value: {value}")

print("\n")

# simple version of this example:
for key, value in user_0.items():
    print(key)
    print(value)

print("\n")

# Nice form could be:
for key, value in user_0.items():
    print(key + ": " + value)
