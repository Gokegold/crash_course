class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@core.com'

    def fullname(self):
        return '{} ' '{}'.format(self.first, self.last)


emp_1 = Employee('Sam', 'Bents', 500000)
emp_2 = Employee('Samon', 'Bent', 700000)

print(emp_2.fullname())
print(emp_2.email)
print(' ')
print(Employee.fullname(emp_1))
print(emp_1.email)


# OR

'''
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

'''
