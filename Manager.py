#Parent class
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display_person(self):
        print(f"Age:{self.age}")

#Parent class 2
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id=emp_id
        self.salary=salary

    def display_employee(self):
        print(f"Employee ID:{self.emp_id }")
        print(f"Salary:{self.salary }")


#Child class inherting from Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        #Initialize parent class
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)

        #Manager-specific attribute
        self.department=department

    #Manager-specific method
    def display_manager(self):
        