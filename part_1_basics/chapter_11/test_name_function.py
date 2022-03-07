# UNIT TEST AND TEST CASES

import unittest
# importing the module unittest from Python libraries
from name_function import get_formatted_name


# Importing the function we want to test

# Create a class for testing - contains series of tests
# name can be anything but it shall say test and relates to the function
# Inheritting the class unittrst.TestCase
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py.'"""

    # naming it like this because we verifying that names with
    # first and last names are formatted correectly
    # within that we call the functions we want to tes
    # any methods startinf with 'test_' will run automatically
    # we asign aruments we want to test to the result (formatted_name)

    def test_first_last_name(self):
        """Do names like Janis Joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        # assert method
        # compares the result of the variable using the function
        #  with the given value
        # as we anticipate formatted_name and Janis Joplin ==


if __name__ == '__main__':
    unittest.main()
