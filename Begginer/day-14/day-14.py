from day_14_data import data
import random

# Say 14 - HigherLower game

random.shuffle(data)
user_score = int() 
user_guess = ""
def set_guess():
    global user_guess
    user_guess = input(f"Do you think {name_a} has more or less followers? Print Higher or Lower to guess\n").lower()


while len(data) > 1:
    name_a = data[0]["name"]
    followers_a = int(data[0]["follower_count"])
    name_b = data[1]["name"]
    followers_b = int(data[1]["follower_count"])
    
    print(f"You're comparing {name_a} against {name_b}")
    set_guess()
    
    compare = bool
    if user_guess == "higher":
        compare = bool(followers_a > followers_b)
    elif user_guess == "lower":
        compare = bool(followers_a < followers_b)
    else:
        print("Oops!You must have misspelled something. Try again.")
        set_guess()
    
    if compare == False:
        print(f"Oh oh, you're wrong. Game over, you're score is {user_score}")
        break
    
    user_score += 1
    print(f"\nYou're right, you're score is {user_score}\n\n")
    
    
    data.pop(0)     

