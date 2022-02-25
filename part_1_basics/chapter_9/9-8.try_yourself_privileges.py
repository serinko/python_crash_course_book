class User:
    """User profile description"""

    def __init__(self, first_name, last_name, age, occupation, middle_name=''):
        """Initialize user attributes"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.occupation = occupation
        self.middle = middle_name

        if self.middle:
            self.name = f"{self.first} {self.middle} {self.last}"
        else:
            self.name = f"{self.first} {self.last}"

    def describe_user(self):
        """Displays a description of user attributes"""
        print(f"\nName: {self.name.title()}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """Displays a greeting to the user"""
        print(f"\nHello {self.name.title()},"
              f"\nhave a nice day with Python programing!")


class Privileges:
    """Stores privileges of a user"""

    def __init__(self):
        """Initialize attributes privileges."""
        self.privileges = []

    def modify_privileges(self, modified_privileges):
        """Modify the list of privileges"""
        self.privileges = modified_privileges

    def show_privileges(self):
        """Displays administrator sets of privileges"""
        privileges_formatted = ", ".join(self.privileges)
        print(
            f"These are the privileges an Admin has: "
            f"{privileges_formatted}."
        )


class Admin(User):
    """A simple attempt to make an admin program"""

    def __init__(
            self, first_name, last_name, age, occupation, middle_name=''
    ):
        """Initialize the attributes of the super class User
         and add initial attributes to the subclass Admin"""

        super().__init__(
            first_name, last_name, age, occupation, middle_name
        )
        self.privileges = Privileges()


admin_0 = Admin('mat', 'c', 13, 'hacker', )
admin_0.describe_user()
admin_0.greet_user()
prgs = [
    'can add post',
    'can delete post',
    'can ban user',
]

admin_0.privileges.modify_privileges(prgs)

admin_0.privileges.show_privileges()
