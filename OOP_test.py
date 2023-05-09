"""
Python crash course

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 7, 2023]

"""


class Vehicle:
    # constructor
    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed

    def camry(self):
        return 'engine' ' ' 'chase'.format(self.mileage, self.max_speed)


# Variable declared outside __init__() belong to the class. They’re shared by all instances.
# create the object(modelx)
# values are passed to the instance variables using a constructor.
modelx = Vehicle(240, 18)
ev = Vehicle(400, 80)

modelx.mileage = 700
modelx.max_speed = 1000

# modify instance variable
ev.mileage = 1000
ev.max_speed = 1000

print('modelx: ', modelx)
print('ev-Max_speed: ', ev.max_speed, ' Ev-Mileage: ', ev.mileage)
print('modelx.max_speed: ', modelx.max_speed, ' Modelx.mileage: ', modelx.mileage)
print(modelx.__dict__)
print('Camry-modelx: ', modelx.camry())

print(' ')
print(Vehicle.camry(modelx))
print(ev.mileage)

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age


# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2 = Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)
