age = 2

print("The age of this person is " + str(age) + ".")

if age < 2:
    print("This is a baby.")
elif age < 4:
    print("This is a toddler.")
elif age < 13:
    print("This is a kid")
elif age < 30:
    print("This is a teenager.")
elif age < 65:
    print("This is an adult.")
else:
    print("This is an elder.")
