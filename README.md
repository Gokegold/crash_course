import math
import random
from pathlib import Path

 
'''
person_name = input("what's your name? ")
Fav_color = input("what's ypur fav color: ")

print(person_name + " likes " + Fav_color)

birth_year = int(input('birth year: '))
age = 2019 - birth_year
print(age)

course = 'ijnfidf dioudyb idndcx'
print(course[0:3])

first = 'jon'
last = 'you'
full_name = f'{first} + {last} is color'
print(full_name)

print(len(course))
print(course.upper())

course = 'fi ioieeo unikp'

print(course.find('unikp'))
print(course.replace('p', 'j'))
print('python' in course)

print(round(x))
print(abs(x))
print(abs(-2.9))

x = 2.9
print(math.ceil(2.9))
print(math.flo)

hot = 5
current_weather = int(input('Enter your current weather: '))

if current_weather < hot:
    print('The weather is hot')
elif current_weather == hot:
    print('the weather is cold')
else:
    print("The weather si okay")


is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes" )
else:
    print('enjoy your day')
    
print("Have you a lovely day")


House_price = 10**6
buyer_credit = int(input("Enter your Credit score: "))
ten_perc = ((10**6) * (10 / 100))

if buyer_credit >= 740:
    print (f"Pay 10% which is: "+ {ten_perc} +" of " +{House_price})
else:
    print (f'20% is needed to be paid')
print('Your Credit is Good')
print(f'Pay a down payment of {ten_perc}')

price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: {down_payment}")

House_Price = 10**2
good_credit = True

if good_credit:
    print('credit is True')
    down_payment = 0.1 * House_Price
else:
    down_payment = 0.2 * House_Price
print(f'down_payment: {down_payment}')

has_good_credit = False
has_high_income = True

if has_high_income or not has_good_credit:
    print("Eligible for loan")

temp = 30

if temp > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")



secret_number = 9
i = 0
while i < 3:
    print



weight = int(input("weight: "))
kg = weight * 0.45359237
lbs = weight / 0.45359237
unit = input("(L)bs or (K)g: ")

if unit == "l" or "L":
    print(f'Your Weight is:  {lbs}')
elif unit == "k" "K":
    print(f'Your Weight is: {kg}')
else:
    print("Invailde unit")


sercet_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == sercet_number:
        print("You have won")
        break
    elif guess_count < guess_limit:
        print("You lost Try again")
    else: 
        guess_count == guess_limit
        print('Game Over')

for items in 'Python':
    print(items)

for items in ['mosh', 'jin', 'dru']:
    print(items)

for i in [1, 2, 3, 4]:
    print(i)

for items in range(5, 10):
    print(items)


prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f'Total: {total}')


decision = input(" > ")
start = 'starting engine and ready to drive...'
stop = 'stoping he car'

if decision == help or 'HELP':
    print(' start - to start the car ')
    print(' stop - to stop the car ')
    print(' to exit ')

if decision == start:
    print("starting engine")


command = ""
started = False
while True:
    command = input(" > ").lower()
    if command == "start":
        if started:
            print("Car is already started !")
        else:
            started = True
            print('Car started...')
    elif command == "stop":
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
    start - to start the car
    stop - to stop the car
    quit - to quit
            """)
    elif command == "quit":
        break
    else:
        print("I don't understand...")
        
for item in range(100):
    print(item)

for items in range(5, 10):
    print(items)

prices = [10, 20, 40]

total = 0
for price in prices:
    total += price
print(f"Total Price: {total}")

for x in range(4):
    for y in range(3):
        for z in range(2):
            print(f'({x}, {y}, {z})')
            
numbers = [0, 4, 4]
for x_count in numbers:
    output =''
    for count in range(x_count):
        output += 'x'
        print(output)


namers = ['jon', 'tom', 'tim', 'rom', 'johness']
names =[1, 2, 4, 5, 3, 6, 7, 9,]
print(namers[2:])
print(namers[2:4])
print(namers[0:])
#names[0] = 'john'

#print(names.max.len[])
max = names[0]
maxi = namers[0]

for namer in namers:
    if namer > maxi:
        maxi = namer
print(maxi)

for name in names:
    if name > max:
        max = name
print(max)

numbers = [2, 3, 4, 4, 5, 5, 2, 8, 8, 9, 3, 3, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

#numbers = [5, 2, 5, 2, 2]
numbers = [3, 3, 3, 3, 6, 6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print(numbers[2:4])

coordinates = (1, 2, 3)
x, y, z = coordinates
#or 

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x, y, z)

customer = {
    "name ": "John Smaith",
    "age ": 30,
    "is_verified ": True
}
print(customer["name "])
print(customer.get("name"))
print(customer.get("Birthday" "jan 1 1980"))
#or
customer["sex"] = "male"

phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

message = input(" > ")

words = message.split(' ')
emojis = {
    ":)":
}
print(words)

def square(number):
    return number * number

print(square(3))

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output


message = input(" > ")
print(emoji_converter(message)) 


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abroad')

print("Start")
greet_user("john", last_name="smith")
print("FINISH")

def square(number):
    return number * number

result = square(3)
print(result)
print(square(3))


def square(number):
    print(number * number)


print(square(3))

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
    

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age connot be 0.')
except ValueError:
    print('Invalid Value')


class Point:
    def move(self):
        print("Move")
    
    def draw(self):
        print("Draw")


point1 = Point()

import converters
from converters import Kg_to_lbs

import Utils
from Utils import find_max

numbers = [1, 2, 3, 6, 10]
find_max()

Kg_to_lbs(100)

print(converters.Kg_to_lbs(70))

import Utils
from Utils import find_max

numbers = [3, 6, 8, 9, 10]
maximum = find_max(numbers)

print(maximum(numbers))

from ecommerce import shipping

shipping.calc_shipping()
from ecommerce.shipping import calc_shipping


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print('hello Cats are annoying')


cat1 = Cat()
cat1.be_annoying()
cat1.walk()


import random



members = ["john", "mary", "TIM", "TOPR"]
leader = random.choice(members)
print(leader)

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))




def dice_one():
    return random.randint(0, 7)


def dice_two():
    for x in range(6):
        return random.randint(0, 7)


numbers = [1, 2, 3, 4, 5, 6]
for x_count in numbers:
    output =''
    for count in range(x_count):
        return random.randrange

def dice1():
    options = (1, 2, 3, 4, 5, 6)
    for option in options:
        return random.choice(options)


class Robot:
    r1 ={
        "name": "Tom",
        "color": "red",
        "weight": 30
    }


    r2 = {
        "name": "Jerry",
        "color": "blue",
        "weight": 40
    }

class Robot:
    def introduce_self(self):
        print("my name is " + self.name)

r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r3 = Robot()
r3.name = "Perry"
r3.color = "Klue"
r3.weight = 40

r1.introduce_self()
r3.introduce_self()


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def introduce_self(self):
        print("My name is + self.first_name + self.last_name")



s1 = Student("Tom", "jan", 20)
s2 = Student("Top", "Ash", 40)      

class Preson:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Talk")


john = Preson("John Smith")
print(john.name)
john.talk()

import random
dice = (1, 2, 3, 4, 5, 6)

dice1 = random.randint(1, 6)

dice2 = random.choice(dice)


print((dice1, dice2))


import random

dice_cube = (1, 2, 3, 4, 5, 6)

dice1 = random.randint(1, 6)

dice2 = random.choice(dice_cube)

print((dice1, dice2))

if dice1 != dice2:
    print("Next Turn")
else:
    print("Roll Again")
    def Dice1():
        roll_two = random.choice(dice_cube)
        return roll_two
    def Dice2():
        roll_two2 = random.randrange(6, 1)
        return roll_two2


print((roll_two, roll_two2))

def play(dice1, dice2):
    start = print("Start Game")
    return start
    def first_dice():
        
        turn = "Next Turn"
        yourTurn = "Roll Again"
        rollAgain = random.choice([1, 2, 3, 4, 5, 6])
    

import random

dice_cube = [1, 2, 3, 4, 5, 6]

def regularPlay():
    
    dice1 = random.choice(dice_cube)
    dice2 = random.choice(dice_cube)
    print((dice1, dice2))
    
    if dice1 == 6 and dice2 == 6:
        print("2-six STILL YOUR TURN")
        dice1 = random.randrange(1, 6)
        dice2 = random.randrange(1, 6)
        print((dice1, dice2))
    else:
        print("NEXT ROLL")
    
regularPlay()


for i in range(1, 11):
    if i % 2 == 0:
        contiune
    print(i)

for i in range(10)
    if i == 0:
        pass
    print(i)
    
string = "hi World"
for char in string:
    print(char)




string = "hello, WORLD!"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string


animals_list = ["cat", "dog", "giraffe", "elephant", "panda"]
animals_tuple = ("cat", "dog", "giraffe", "elephant", "panda")

for animal in animals_list:
    print(f"{animal}s are cute")


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())




from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)


'''

