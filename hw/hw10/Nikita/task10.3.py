class Employee:
    """Info about employees"""
    amount_of_employees = 0  

    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
        Employee.amount_of_employees += 1
    
    @classmethod
    def get_amount_of_employees(cls):
        return f'Total employees: {cls.amount_of_employees}'
    
    def info(self):
        return f"Employee's name: {self.name}, Employee's salary: {self.salary}"

employee1 = Employee(salary=50000, name='Ivan')
employee2 = Employee(salary=60000, name='Nikita')

print(employee1.info())
print(employee2.info())

print(Employee.get_amount_of_employees())

print(f'Base: {Employee.__bases__}')
print(f'Dict: {Employee.__dict__}')
print(f'Name: {Employee.__name__}')
print(f'Module: {Employee.__module__}')
print(f'Doc: {Employee.__doc__}')





        