import random

#  Day 12 - Number guessing game

user_tries = int()
user_guess = int()
def set_difficulty():
    global user_tries
    diff = input("What level of dificulty would you like to choose? You can set it to:\n Easy - 10 tries\n Medium - 5 tries\n Hard - 3 tries\n\n").lower()
    if diff == "easy":
        user_tries = 10
    elif diff == "medium":
        user_tries = 5
    elif diff == "hard":
        user_tries = 3
    else:
        set_difficulty()
    print(f"You have {user_tries} guesses")
def set_user_guess():
    global user_guess
    user_guess = int(input("What's the number?\n"))
    global user_tries 
    user_tries -= 1


the_answer = random.randint(0,100)
print(the_answer)

set_difficulty()
set_user_guess()
def set_winner():
    if user_guess == the_answer:
        print("You have won!")
    if user_guess != the_answer and user_tries == 0:
        print("Sorry you lost")


while user_guess != the_answer and user_tries != 0:
    print(f"Oh oh, that's wrong\nYou have {user_tries} guesses left")
    set_user_guess()
set_winner()