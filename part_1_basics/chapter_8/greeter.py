# The function definition using def funtion_name():
# Function definition is marked with the colon in the end

def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    # All the indented lines make the body of the function
    # The """ text """ is a "docstring" - describing what function does


greet_user()


# A call for the function - Python executes that


# Adding a value into paranthesis
# Python expects me to define the value later
def greet_user(username):  # username is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
    # Using the value further as a variable in f-string


greet_user('maria')
# If we did not  define the value, the function would not work
# in other words. The function does not work job without the parameter needed
# THIS TYPE OF PARAMETER WE CALL ARGUMENT
# AN ARGUMENT IS PASSED FROM FUNCTION CALL TO A FUNCTION
