# try-except blocks

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Because 5/0 returns ZeroDivisionError: division by zero
# We set up an exception
