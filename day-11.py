import numpy as np
# Day 11 - Blackjack
cards = int()
pool = list(range(1,11)) + [10] * 3  # adds 4 tens, 1 as a ten, 1 as jack, 1 as queen, 1 as king
def random_card():
    global cards
    global pool
    cards = np.random.choice(pool)
    pool.remove(cards)
    print(pool)
    

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
    print(u_cards,u_result,c_cards, c_result, winner)

# For now is fully random
start()
winner_is()