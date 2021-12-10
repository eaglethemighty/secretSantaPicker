
class Person:
    name: str
    email: str

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        isEqual = self.name == other.name
        return isEqual

    def __str__(self):
        return self.name
