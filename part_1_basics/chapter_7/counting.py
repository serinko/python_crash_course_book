# while loop, runs through a condition as long as the statement is true
#
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# in first line we start counting from 1
# the while loop is set to run as long sas the number <= 5
# the code inside the while loop prints the current number and then
# (+=) adds 1, making the current_number value = 2
# compraes it with the while parameters and repeats until
# the while statement is not true

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
# First we entered current number as 0 value
# It is < 10 so the while loop started
# Every loop it increments of 1 (+)
# Then the modulo function checks if after diving by two, left == 0
# in other words if current number is divisible by 2
# continue function tells Python to ignore the rest of the loop
# meaning - returns to the beginning
# If its not divisible by 2, Pyton continues and prints the number
# = Odd number.
