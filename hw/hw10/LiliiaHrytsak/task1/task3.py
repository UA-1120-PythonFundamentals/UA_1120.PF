class Employee():
    counter = 0

    def __init__(self, name, salary):
        self.salary = salary
        self.name = name
        Employee.counter += 1

    def displ_info(self):
        print(f'Name of employee is {self.name}\nSalary of employee is {self.salary}\n')

    @classmethod
    def displ_total_employee(clf):
        print( f'Total number of employee is {Employee.counter}')


a = Employee('a',100)
a.displ_info()
b = Employee('b',200)
b.displ_info()
c = Employee('c',400)
c.displ_info()

Employee.displ_total_employee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)



