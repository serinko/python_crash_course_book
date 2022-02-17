prompt = "Please enter a number and we can see if it's a multiple of 10: "
number = input(prompt)
number = int(number)

if number % 10 == 0 and number != 0:
    print(f"\nNumber {str(number)} is a multiple of 10.")
else:
    print(f"\nNumber {str(number)} is not a multiple of 10.")
