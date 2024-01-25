class Employee:

    total_employees = 0

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: ₴{self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.total_employees}")

worker1 = Employee("Andriy", 1000)
worker2 = Employee("Vasyl", 2000)
worker3 = Employee("Alina", 3000)
worker4 = Employee("Yulia", 4000)

worker1.display_info()
worker2.display_info()
worker3.display_info()
worker4.display_info()

Employee.display_total_employees()

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")