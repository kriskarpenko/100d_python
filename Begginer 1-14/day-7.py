# Day 7 - hangman game

import random
word_list = ["apple", "banana", "cherry", "dorian", "fig"]

the_word = random.choice(word_list) # word that should be guessed
lttr_in_the_word = [lttr for lttr in the_word]
word_length = len(the_word) #used to find double letters in a word
amount_of_guesses = word_length
hidden_word = '' # var to have _ instead of letters
hidden_letter = []
lttr_used = []

for lttr in the_word:
    hidden_word += '_'
hidden_letter = [lttr for lttr in hidden_word]
print(f"Hi there, are you ready to guess the word?\nHere is a hint: {hidden_word}")

# Setting an input as a var and being able to recall it
guess = input("Take a guess\n").lower()
def take_guess():
    global guess
    guess = input("Take another guess\n").lower()

# Enumerate function acts as an index identifier
# then if the letters in hidden word and user input match, the user input replaces "_"
# Catches the duplicate letters via loop with idx - index
def reveal_lttr(inp):
    for idx, lttr in enumerate(lttr_in_the_word):
        if lttr == inp:
            hidden_letter[idx] = inp
    global hidden_word
    hidden_word = ''.join(hidden_letter)
    print(f"Updated word: {hidden_word}")


while amount_of_guesses > 0:
    if guess in lttr_used:
        print("Oops, you have already tried this letter")
        take_guess()
    elif guess in lttr_in_the_word:
        lttr_used += guess
        reveal_lttr(guess)
        if "_" not in hidden_letter: # is embeded to prevent asking for another guess after the word is completed
            print(f"Congratulations! You have guessed the word - {the_word}. You've won.")
            print(f"These are the letters you have used: {lttr_used}")
            break
        print(f"You're right. These are the letters you have used: {lttr_used}")
        take_guess()
    else:
        amount_of_guesses -= 1
        lttr_used += guess
        print(f"You're wrong. These are the letters you have used: {lttr_used}")
        take_guess()

if "_" in hidden_word:
    print(f"Game over. The word was {the_word}. You've lost.")
    print(f"These are the letters you have used: {lttr_used}")