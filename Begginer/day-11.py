import random
# Day 11 - Blackjack

cards = int()
pool = list(range(2,12)) + [10] * 3  # adds 3 tens at the end, 1 as jack, 1 as queen, 1 as king
print(pool)
determine_10 = ["10","j","q","k"] # a list with string to assign to 4 tens in the pool. Will only be used for print
def random_card():
    global cards
    global pool
    cards = random.choice(pool)
    pool.remove(cards)
    

# all of the user vars
u_output = []
u_cards = []
u_result = int()
    
# all fo the computer vars
c_output = []
c_cards = []
c_result = int()

add_card = "yes"

def set_cards(some_cards:list[int], some_output:list[str]):
    random_card()
    some_cards.append(cards)
    result = sum(some_cards)
    if cards == 10:
        determined = random.choice(determine_10) # randomly selects if the player got 10, j, q or k
        some_output.append(determined)
        determine_10.remove(determined)
    else:
        some_output.append(str(cards))
    return result

    # if cards == 11

def start():
    for x in range(0,2):
        set_cards(u_cards, u_output)
        u_result = sum(u_cards)
        
    for x in range(0,2):
        set_cards(c_cards, c_output)
    print(f"Welcome to Blackjack your hand is: {u_output}, your score is: {u_result}")
    print(f"Computer's card is: {c_output[0]}")

def winner_is():
    winner = ""
    u_result = sum(u_cards) 
    c_result = sum(c_cards)
    if u_result == 21:
        winner = "User got Blackjack"
    if c_result == 21:
        winner = "Computer got Blackjack"
    if u_result < 21:
        if u_result > c_result:
            winner = f"User won by {u_result-c_result} points."
        elif u_result == c_result:
            winner = "It's a draft"
        elif c_result > 21:
            winner = "User won"
        else:
            winner = "Computer won"
    elif u_result > 21:
        winner = "Computer won"
    
    print(f"Finall results are:\n {winner}\n Computer's score is {c_result}, computer's cards were {c_output}\n User's score is {u_result}, user's cards were {u_output}")


start()
while add_card == "yes" and u_result < 21:
    u_result = sum(u_cards)
    c_result = sum(c_cards)
    if u_result == 21:
        print("User got Blackjack")
        break
    if c_result == 21:
        print("Computer got Blackjack")
        break
    if u_result > 21:
        print(f"Oh, oh you've gone overboard, your score is {u_result}")
        break
    if c_result > 21:
        print(f"Oh, oh computer has gone overboard, the score is {c_result}")
        break
    add_card = input("Would you like to get another card?").lower()
    if add_card == "yes" and u_result < 21:
        set_cards(u_cards, u_output)
        u_result = sum(u_cards)
        if u_result > 21:
            print(f"Oh, oh you've gone overboard, your score is {u_result}")
            break
        print(f"You just drew {u_output[-1]}. Your cards now are{u_output}, your current score is {u_result}")  
    if add_card == "no" and len(u_cards) > 2:
        set_cards(c_cards, c_output)
        c_result = sum(c_cards)
winner_is()