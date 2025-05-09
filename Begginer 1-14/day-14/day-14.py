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


"""
Thought process:
    1. figured out how to get name_a and name_b from data in a for loop
    2. for loop was unnecessary and it was impossible to get rid of the already "used" first option so i switched to while
    3. last option becomes the first one, so the data[0] should be removed after the round is over
    4. at first i thought to complete as it is shown in the demo from the course to pick A or B, but I decided to make it as
        usual game so i implemented options "higher" or "lower". if user selects "higher" the followers of the first option 
        are considered to be higher and vice versa
    5. make those comparisons return a boolean, if boolean has a false value break the loop
    6. make a global user_score variable so it is not being overwritten in the loop; adding +1 to score every round
    7. setting user guess into a function so i can get eliminate all of the misspelling scenarios
"""