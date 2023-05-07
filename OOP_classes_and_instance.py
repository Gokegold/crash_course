

class Employee:

    num_of_emps = 0
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

    # to turn a regular method to a Class_methods you use the decorator 'classmethod'
    #
    @classmethod
    # the conventional method takes the instance as the first argument which is 'self'
    # But class_method uses the cls instance
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Sam', 'Bents', 500000)
emp_2 = Employee('Samon', 'Bent', 700000)


print(emp_2.__dict__)
print(emp_1.raise_amt)
print(Employee.raise_amt)
print(Employee.num_of_emps)

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

"""

Employee.set_raise_amt(2.00)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
