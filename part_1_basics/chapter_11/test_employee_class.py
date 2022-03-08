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
        self.amount = 9500

    def test_give_raise_default(self):
        """Test default give raise default value"""
        self.employee.give_raise()
        self.assertEqual(
            self.employee.salary_raised,
            self.employee.salary + self.employee.amount
        )

    def test_give_raise_custom(self):
        """Test default give raise custom value"""
        self.employee.give_raise(self.amount)
        self.assertEqual(
            self.employee.salary_raised,
            self.employee.salary + self.employee.amount
        )


if __name__ == '__main__':
    unittest.main()

