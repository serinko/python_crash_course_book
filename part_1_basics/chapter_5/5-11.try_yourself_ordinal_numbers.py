ordinal_numbers = list(range(1, 10))
# print(ordinal_numbers)

for number in ordinal_numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
