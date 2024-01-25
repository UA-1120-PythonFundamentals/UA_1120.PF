#!/usr/bin/env python


class Employee:
    """Employee info: name and salary. Consists information about how many employees are there."""

    employee_counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1

    def total(self):
        print(f"Total employees: {Employee.employee_counter}")

    def employee_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

    @staticmethod
    def cls_info():
        _base = Employee.__base__
        _dict = Employee.__dict__
        _name = Employee.__name__
        _module = Employee.__module__
        _doc = Employee.__doc__
        print(
            f"Base class: {_base}\nClass dict: {_dict}\nClass name: {_name}\nModule name: {_module}\nClass docstring: {_doc}"
        )


if __name__ == "__main__":
    e1 = Employee("Jimmy", 100)
    e1.total()
    e1.employee_info()

    e2 = Employee("Diana", 200)
    e2.total()
    e2.employee_info()

    e2 = Employee("Gorge", 300)
    e2.total()
    e2.employee_info()

    print("\n\n\nInformation about Employee class:")
    Employee.cls_info()
