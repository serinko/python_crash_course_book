# FORMATING OF VARIABLES IN STRINGS
# THE SECOND EDITION OF THE BOOK IS DIFFERENT:
# The introduce method is called F-STRINGS
# Instead of: variable_0 + variable_1
# The new way is: f"{variable_0} {variable_1}"
# where "f" stands for format.
# In practice it can look like this:

# Crash Course Book - edition 1:
variable_0 = "This is the way we used in the edition: "
variable_1 = "ONE"
message_one = variable_0 + variable_1

print(message_one)

# Crash Course Book - edition 2:
variable_0 = "This is the way we used in the edition: "
variable_2 = "TWO"
message_two = f"{variable_0} {variable_2}"
# the "" are quite confusing in this new format.
# the "quotations "  mark the f-string beginning and end
# no + sign used, just space, for easier reading (styling the code)
print(message_two)

# This can be done with longer strings as well, for example
name = 'leo'
surname = 'peltier'
full_name = f"{name} {surname}"
print(f"Sending you my love, {full_name.title()}.")
# only 'f' stayed before the "quotations"
# no + sign
# .title in {} together with the variable
# Everything (but 'f') within "quotations" to mark/define it as one string
# all of that in print(brackets)
