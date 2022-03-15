class Parent:
    """A parent class"""

    def __init__(self):
        self.foo = "hello"
        self.child = Child(self)


class Child:
    """A child class"""

    def __init__(self):
        self.parent = Parent()
