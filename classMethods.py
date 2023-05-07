# classmethod and staticmethod

# Functions and arguments
# functions are defined with 'def' and must be ended with a column ':' just before '()'
# then followed by the name if the function
# And a set of formal parameters
# actual parameters or arguments are passed during a function call
# (i.e) actual parameters and arguments when the function is called
###
# functions can be defined with variable number of arguments.

# Example:
# def realtors(arg1, arg2)
#   functions statements are written

#   realtors(a,b)

###
# def -- defines realtors as to be a function
# arg1 and arg2 are the formal parameters

# realtors(a,b) here the function is called
# (a, b) are the actual parameter or arguments

###

# Function types

# DEFAULT ARGUMENTS


def add(a, b=5, c=10):
    return a+b+c


'''

Default arguments are values that are provided while defining functions.
The assignment operator = is used to assign a default value to the argument.
Default arguments become optional during the function calls.
If we provide a value to the default arguments during function calls, it overrides the default value.
The function can have any number of default arguments.
Default arguments should follow non-default arguments.

'''
###
# GIVING ONLY THE MANDATORY ARGUMENT
print(add(3))

# GIVING ONLY THE OPTIONAL ARGUMENTS
print(add(3, 4))

# GIVING ALL THE MANDATORY ARGUMENT
print(add(2, 3, 4))


###
# functions can be called by using keyword arguments
# that is keyword=value (of keyword)
# see below


def add(a, b=5, c=10):
    return a + b + c


# there is no need to maintain the same order is the formal argument passed
# the keyword parameter makes this easier
# 'b' is the keyword and "10" the value of the keyword

print(add(b=10, c=15, a=20))

# note the function add has an argument that has no keyword value which is 'a'
# which mean it can be assigned a value when the add function is call
# this is the DEFAULT optional ARGUMENT type
print(add(a=10))


# output will be 25 (i.e) a=10 + b=5 + c=10

###
# POSITIONAL ARGUMENT
# During a function call
# Values passed through arguments should be in the order of parameters in the defined function
# (i.e) THE SAME WAY IT PASSED IN THE FUNCTION IS THE SAME WAY IT HAS TO BE WHEN CALLING FUNCTION
# EXAMPLE:


def add(a, b, c):
    return a + b + c


# values passed in the argument are passed to parameters or FORMAL ARGUMENTS by their position
print(add(10, 20, 30))
# note a=10 b=20 c=30
# finally keyword arguments do not require same order of argument positioning as to positional arguments

###

# Variable-length Arguments
###
'''
Variable-length arguments are also known as arbitrary arguments. 
If we don’t know the number of arguments needed for the function in advance, 
we can use arbitrary arguments
'''

###

'''
THERE ARE TWO TYPES OF ARBITRARY ARGUMENTS:
Arbitrary positional arguments.
Arbitrary keyword arguments.


ARBITRARY POSITIONAL ARGUMENTS IN PYTHON
For arbitrary positional argument, 
an asterisk (*) is placed before a parameter in function definition 
"WHICH CAN HOLD NON-KEYWORD VARIABLE-LENGTH ARGUMENTS."
These arguments will be wrapped up in a tuple. Before the variable number of arguments, 
zero or more normal arguments may occur.
'''


# Example:


def add(*b):
    result = 0
    for i in b:
        result = result + i
    return result


print(add(1, 2, 3, 4, 5))

print(add(10, 20))

"""
ARBITRARY KEYWORD ARGUMENTS IN PYTHON
For arbitrary positional argument, 
A DOUBLE ASTERISK (**) IS PLACED BEFORE A PARAMETER IN A FUNCTION 
which can hold keyword variable-length arguments.
"""


def fn(**a):
    for i in a.items():
        print(i)


fn(numbers=5, colors="blue", fruits="apple")

# Output:
# ('numbers', 5)
# ('colors', 'blue')
# ('fruits', 'apple')
