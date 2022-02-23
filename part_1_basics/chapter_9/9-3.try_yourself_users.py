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


user_0 = User('pepe', 'frog', 19, 'meme', 'the')
user_0.describe_user()
user_0.greet_user()

user_1 = User('jesus', 'christ', 33, 'prophet')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Mazlum', 'dogan', 25, 'revolutionary')
user_2.describe_user()
user_2.greet_user()

user_3 = User('anna', 'brave', 78, 'healer', 'brigid')
user_3.describe_user()
user_3.greet_user()
