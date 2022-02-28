# READING FROM A FILE

# 1) READING AN ENTIRE FILE:
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
