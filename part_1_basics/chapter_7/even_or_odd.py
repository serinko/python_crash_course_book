# UIsing a modulo (%) function
# it gives us a reminder after we divide one number by naother
# if we divide by 2 and reminder is 0 (%2==0), the number is even
prompt = "Enter a number, and I'll tell you if it's even or odd: "
number = input(prompt)
number = int(number)

if number % 2 == 0:
    print(f"The number {str(number)} is even.")
else:
    print(f"The number {str(number)} is odd.")
