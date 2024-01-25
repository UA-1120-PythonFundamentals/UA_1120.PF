class Employee:
    total = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total += 1

    @classmethod
    def print_total(cls):
        return f"Total number of employees = {cls.total}."

    def display_info(self):
        return f"Name: {self.name}\nSalary: {self.salary}"

    def class_info():
        return f"Base classes: {Employee.__base__}\nNamespace: {Employee.__dict__}\nClass name: {Employee.__name__}\nModule name: {Employee.__module__}\nDocumentation: {Employee.__doc__}"
