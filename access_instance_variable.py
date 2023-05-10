"""
Ways to Access Instance Variable

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 7, 2023],[May 7, 2023]

"""


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
# ACCESS INSTANCE VARIABLE USING getattr()
# To gain access into ACCESS VARIABLE
