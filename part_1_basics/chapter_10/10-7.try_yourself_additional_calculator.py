print("Give me two numbers and I'll add them.")
print("(Enter 'q' to quit!)")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

        print(f"{a} is not a number.")
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        a = int(first_number)
    except ValueError:
        print(f"{a} is not a number.")

    try:
        b = int(second_number)
    except ValueError:
        print(f"{b} is not a number.")
    else:
        answer = a + b
        print(f"\nThe answer is {answer}.")
