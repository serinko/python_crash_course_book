"""
A module with sub class Admin, imported super class USer and class Privileges
"""

from module_class_admins import User


class Privileges:
    """Stores privileges of a user"""

    def __init__(self, privileges=[]):
        """Initialize attributes privileges."""
        self.privileges = privileges

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
