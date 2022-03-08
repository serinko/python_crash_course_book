import unittest
from class_Employee import Employee


class TestEmployeeClass(unittest.TestCase):
    """Test class for the class employee"""

    def setUp(self):
        """Create an instance of an employee for the test"""
        first = 'Karel'
        second = 'Rendl'
        salary = 24000
        self.employee = Employee(first, second, salary)
       