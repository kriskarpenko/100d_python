import numpy as np
# Day 11 - Blackjack
cards = int()
def random_card():
    global cards
    cards = np.random.randint(0,10)

u_cards = []
u_result = int()
def set_u_cards():
    random_card()
    u_cards.append(cards)
    global u_result
    u_result += cards 
c_cards = []
c_result = int()
def set_c_cards():
    random_card()
    c_cards.append(cards)
    global c_result
    c_result += cards 

def start():
    for u in range(0,2):
        set_u_cards()    
    for c in range(0,2):
        set_c_cards()

    
def winner_is():
    winner = ""
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
    print(u_result, c_result, winner)

# For now is fully random, work on adding 10 points 4 times
start()
winner_is()