class Employee:
    """A simple modeling of an employee"""

    def __init__(self, first, second, salary):
        """Stores name and salary"""
        self.fist = first
        self.second = second
        self.salary = salary

    def give_raise(self, amount=5000):
        self.amount = amount
        self.salary_raised = self.salary + self.amount
