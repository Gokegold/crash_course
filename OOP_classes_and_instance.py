x = 1
print(type("HELLO"))
# 'hello' is an object of the class string


def hello():
  print('hello')
# Object of the class function

#methods can be preformed on object or acts on object

string = "hello"
print(string.upper())

# the class function is like a blueprint for a method
# a method is a function that goes inside a class, and alway begins with a parameter slef.
# class can both store method ad store actions to be taken
# we can call for the actions in a class
#... By calling instance.themethod() and print no need to pass any agument into the method 
#.... Or call the class.themethod(and pass the instance here)

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
