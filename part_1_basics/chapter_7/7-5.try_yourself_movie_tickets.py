# movie theater changes tickets according age
# under 3 years, ticket is free
# between 3 and 12, ticket is 10$
# over 12, ticket is $10

prompt = "Welcome to our cinema. How old are you? "
age = input(prompt)
age = int(age)

if age < 121:
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age <= 120:
        price = 15
    message = "Your ticket price is: "
    print(f"{message}{str(price)}")
else:
    print("Do you think we are stupid? Make fun of yourself!")
