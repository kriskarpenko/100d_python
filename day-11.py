import random
# Day 11 - Blackjack

cards = int()
pool = list(range(1,11)) + [10] * 3  # adds 4 tens, 1 as a ten, 1 as jack, 1 as queen, 1 as king
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


def set_cards(some_cards:list[int], some_output:list[str]):
    random_card()
    some_cards.append(cards)
    if cards == 10:
        determined = random.choice(determine_10)
        some_output.append(determined)
        determine_10.remove(determined)
    else:
        some_output.append(str(cards))

def start():
    for x in range(0,2):
        set_cards(u_cards, u_output)
        
    for x in range(0,2):
        set_cards(c_cards, c_output)

add_card = "yes"
def more_cards():
    global add_card
    u_result = sum(u_cards)
    print(f"Hi, your cards are{u_output}, your current score is {u_result}")  
    add_card = input("Would you like to get another card?").lower()
    if add_card == "yes":
        set_cards(u_cards, u_output) 


def winner_is():
    winner = ""
    u_result = sum(u_cards) 
    c_result = sum(c_cards)
    if u_result < 21:
        if u_result > c_result:
            winner = "user"
        elif u_result == c_result:
            winner = "draft"
        else:
            if c_result < 21:
                winner = "user"
            winner = "computer"
    elif u_result > 21:
        winner = "computer"
    print(u_cards,u_result,u_output, c_cards, c_result, c_output, winner)

# works but i want the game to stop when the user goes over 21
start()
while add_card == "yes" and u_result <= 21:
    more_cards()
winner_is()