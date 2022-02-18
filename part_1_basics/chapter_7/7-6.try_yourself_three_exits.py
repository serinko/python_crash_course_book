prompt = "Welcome to our cinema. How old are you? "
age = input(prompt)
age = int(age)

while age < 120:
    if age < 3:
        price = 0

    elif age <= 12:
        price = 10
    elif age <= 120:
        price = 15
    message = "Your ticket price is: "
    print(f"{message}{str(price)}")
    break
