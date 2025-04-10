import random

#  Day 12 - Number guessing game

user_guess = int()
def set_user_guess():
    int(input("What's the number?"))

the_answer = random.randint(0,100)
print(the_answer)

set_user_guess()