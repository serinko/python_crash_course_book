# try-except blocks

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Because 5/0 returns ZeroDivisionError: division by zero
# We set up an exception
# Further code continues running because Python handled the error

# USING EXCEPTIONS TO PREVENT CRASHES

print("Give me two numbers and I''ll divide them.")
print("(Enter 'q' to quit!)")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number_ = input("\nSecond number: ")
    if second_number_ == 'q':
        break

    answer = int(first_number) / int(second_number_)
    print(answer)

    