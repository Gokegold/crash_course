# # #madlibs
# # youtuber = '@jameskoko'
# # print('subscribe to ' +  youtuber)
# # print('subscribe to {}'.format(youtuber))
# # print(f'subscribe to {youtuber}')


# adj = input('Adjective: ')
# verb1 = input('Verb: ')
# verb2 = input('Verb: ')
# famous_person = input('Famous person: ')

# madlib = f'computer programming is so {adj}! It makes me so exicted all the time becasue \
# i love to {verb1}. Stay hydrsted and {verb2} like you are {famous_person}!'
# print(madlib)

#Guessing NUmber
import random

 def guess (x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a between 1 and {x}: '))

        if guess%2 == 0 and guess < random_number:
            print(f'{guess} the guessed number is EVEN and LOW')
        elif guess%2 != 0 and guess > random_number:
            print(f'try again {guess} is ODD and HIGH')
        elif guess%2 == 0 and guess > random_number:
            print(f'Try again {guess} is EVEN and High')
        elif guess%2 != 0 and guess < random_number:
            print(f'Try again {guess} is ODD number and LOW')

    print(f'Guessed number is: {random_number}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        
        else:
             guess = low
             
        feedback = input(f' Is {guess} too high (H), too low (L), or correct(c)?? ').lower
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

print(f' computer guess number {guess} correctly! ')


guess(10)
