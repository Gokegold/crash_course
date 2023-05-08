"""
Python crash course

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

Date modified: May 8, 2023

"""


class Employee:

    num_of_emps = 0
    # This is a class variable
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@core.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} ' '{}'.format(self.first, self.last)

    def appy_raise(self):
        # when accessing class variable or variable in a class we can do that through
        # Class itself (in this case its Employee) OR the instance of the class (in the case it's the 'self')
        # leaving it as self.
        self.pay = int(self.pay * self.raise_amt)

    # to turn a regular method to a Class_methods you use the decorator 'class-method'
    #
    @classmethod
    # the conventional method takes the instance as the first argument which is 'self'
    # But class_method uses the cls instance
    def set_raise_amt(cls, amount):
        # The raise.amount here is class variable for the class.method
        cls.raise_amt = amount

    # Now using class-method as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        # We now have new employee needed to be attributed to the employee class
        # They come in a dash splitting format
        # And this will require a new splitting method understandable by the Employee class.
        first, last, pay = emp_str.split('-')
        # the employee object has to be returned, so it can be accessible when it is called
        return cls(first, last, pay)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# splitting the string up into looking like the Employee __init__ attribute the (parent Class)
first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)


# INHERITANCE
class Developer(Employee):
    # Inheriting from the employee class
    raise_amt = 1.10
    # This changes the raise amount in the Developer subclass
    # Yet affection nothing
    # The raise amount here is for the developer

    def __init__(self, first, last, pay, prog_lang):
        # because we need to pass in another attribute in the __init__ method
        # we let Developers __init__ emulate the Employee __init__ method using super().__init__
        super().__init__(first, last, pay)
        # we pass in the prog_lang for the Developer class
        self.prog_lang = prog_lang
        # Because we have no attributes in the developer class,
        # (i.e) no __init__ method function or empty class
        # when the output is to be printed or class Developer reff
        # Python will move up the command chain in search of the attributes


class Manager(Employee):
    # Thus is a class variable
    raise_amt = 2.0

    def __init__(self, first, last, pay, employees=None):
        # Super().__init__ means copy the __init__ of the class to inherit from
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # To add employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # To remove employees
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # To print employee
    def print_emp(self):
        for emp in self.employees:
            print('>>>', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 80000, 'python')
dev_2 = Developer('Test', 'Employee', 60000, 'java')

mgr_1 = Manager('smith', 'Sue', 100000, [dev_1])
# mgr_2 = Managers('Test', 'Employee', 60000, 'java')

print(mgr_1.email)

# The help function helps visualize the class
# print(help(Developer)

emp_1 = Employee('Sam', 'Bents', 500000)
emp_2 = Employee('Samon', 'Bent', 700000)

print(dev_1.prog_lang)
print(dev_2.prog_lang)
# To print out as a dictionary
'''
print(emp_2.__dict__)
print(emp_1.raise_amt)
print(Employee.raise_amt)
print(Employee.num_of_emps)

'''
"""

print(emp_2.fullname())
print(emp_2.email)
print(' ')
print(Employee.fullname(emp_E1))
print(emp_1.email)


# OR


class Employee:
    def fullname(self):
    return '{} ' '{}'.format(self.first, self.last)


emp_1.first = 'Cort'
emp_1.last = 'cart'
emp_1.email = 'cort.cart'
emp_1.pay = 57000

emp_2.first = 'Corty'
emp_2.last = 'Cat'
emp_2.email = 'corty.cat'
emp_2.pay = 700000

emp_1 = Employee()
emp_2 = Employee()
Employee.set_raise_amt(2.00)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
"""
