class employee:
    # test
    """Data employees"""
    def __init__(self):
       self.employees = []
    def totalCount(self):
       all_name = self.employees.len()
       print(f"Count employees : {all_name}")
    def getEmployees(self):
       print(f"Information : {self.employees}")
       # name , salary for each employee
    def addEmployee(self, name, salary):
        self.employees.append([name, salary])  

a = employee()
while input("if you have employees - enter any, but if haven't - Enter : "):
    enter_employee = input("Enter name : ")
    enter_salary = input("Enter salary : ")
    a.addEmployee(enter_employee,enter_salary)
 
a.totalCount()
a.getEmployees()
print(a.__module__)
print(a.__dict__)
print(a.__doc__)
print(a.__class__.__base__)  
print(a.__class__.__name__)