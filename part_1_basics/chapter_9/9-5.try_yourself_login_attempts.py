class User:
    """User profile description"""

    def __init__(self, first_name, last_name, age, occupation, middle_name=''):
        """Initialize user attributes"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.occupation = occupation
        self.middle = middle_name
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increases login attempts by 1, with every attempt"""
        self.login_attempts += 1

    def read_login_attempts(self):
        """Displays count of the login attempts by the user."""

        print(
            f"{self.name.title()}, you have tried to log-in "
            f"{self.login_attempts} times."
        )

    def reset_login_attempts(self):
        """Resets the login attempts number to 0."""
        self.login_attempts = 0


user_0 = User('pepe', 'frog', 19, 'meme', 'the')
user_0.increment_login_attempts()
user_0.read_login_attempts()
user_0.increment_login_attempts()
user_0.read_login_attempts()
user_0.increment_login_attempts()
user_0.read_login_attempts()
user_0.reset_login_attempts()
user_0.read_login_attempts()
user_0.describe_user()
user_0.greet_user()
