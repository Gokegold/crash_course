"""
Create Instance Variables

Ways to Access Instance Variable

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 9, 2023],[May 10, 2023]

"""
# Instance variables are declared inside a method using the self keyword.
# We use a constructor to define and initialize the instance variables.
# Let’s see the example to declare an instance variable in Python.

# EXAMPLE ONE

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
# Output = <__main__.Student object at .......>
print('Name:', s1.name)
# output = Name: Jesse
print('Age:', s1.age)
# Output = Age: 20

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
# Output = Name: Kelly
print('Age:', s2.age)
# Output = Age: 10

# WAYS TO ACCESS INSTANCE VARIABLE

"""
There are two ways to access the instance variable of class:

Within the class in instance method by USING THE OBJECT REFERENCE (self)
Using getattr() method
"""


# USING THE OBJECT REFERENCE
# EXAMPLE ONE
class Student:
    # The 'def' function as a constructor
    # nom, sex, percentage are the Parameters to construct
    def __init__(self, nom, sex, percentage):
        # INSTANCE VARIABLE
        self.nom = nom
        self.sex = sex
        self.percentage = percentage

    # Here is the INSTANCE METHOD
    # the behavior of the class Student and how the format of how th object will act
    # Instance method access instance variable
    def show(self):
        print("Students Name is,", self.nom, "and Student is a,", self.sex, "With a percentage of", self.percentage)


# Create object
# The object to the class Student
stud = Student
# The instances of the object stud
jesse = Student('Jesse', 'Female', '15%')
# Call instance method
stud.show(jesse)


# EXAMPLE TWO
# USING getattr(object, Parameters in the constructor
"""
ACCESS INSTANCE VARIABLE USING getattr()
To gain access into ACCESS VARIABLE
"""

# EXAMPLE TWO
"""
ACCESS INSTANCE VARIABLE USING getattr()
To gain access into ACCESS VARIABLE
    Pass the object reference and instance variable name to the getattr() method...
    ...to get the value of an instance variable.
    
    getattr(Object, 'instance_variable')
"""


class Pupils:
    # constructor
    def __init__(self, noms, ages):
        # Instance variable
        self.noms = noms
        self.ages = ages


# create object
pupil = Pupils("Jesse", 20)

# Use getattr() to access the values of the instance variable
print('Name: ', getattr(pupil, 'noms'))
print("AGE: ", getattr(pupil, 'ages'))


# INSTANCE VARIABLES NAMING CONVENTIONS
"""
    Instance variable names should be all lower case. For example, 'id'
    Words in an instance variable name should be separated by an underscore.
    # FOR EXAMPLE, store_name
    Non-public instance variables should begin wth a single Underscore
    if an instance needs to bee mangled, two underscores may begin its name
"""
# DYNAMICALLY ADD INSTANCE VARIABLE TO A OBJECT
"""
    We can add instance variables from the outside of class to a particular object.
    Use the following syntax to add the new instance variable to the object
    object_referance.variable_name = value
"""


# EXAMPLE:
class Apprentice:
    # Instance variable
    def __init__(self, names, ages):
        self.names = names
        self.ages = ages


# create object
app = Apprentice('JONES', 21)

print('Before')
print('Name:', app.names, 'AGES:', app.ages)

# add new instance variable 'scores' to app
app.scores = 75
print('After')
print('Name:', app.names, 'AGES:', app.ages), 'SCORES:', app.scores)

"""
    ALL OUTPUT
        Name:  Jesse
        AGE:  20
        
        Before
        Name: JONES AGES: 21
        
        After
        Name: JONES AGES: 21
        SCORES: 75
"""

