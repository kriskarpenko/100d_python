# Day 9 - blind auction

name = ""
def set_name():
    global name 
    name = input("What's your name?\n")
bid = int()
def set_bid(): #Only accepts numbers
    global bid 
    bid = input("How much would you like to bid?\n$")
    try:
        int(bid)
    except ValueError:
        try:
            float(bid)
        except ValueError:
            print("This is not a number. Please try again")
            set_bid()
other_bidders = "yes"
def set_bidders():
    global other_bidders
    other_bidders = input("Are there any other bidders\n").lower()

bids ={}

while other_bidders == "yes":
    set_name()
    set_bid()
    set_bidders()
    print("\n"*13)
    bids[name] = bid


def winner_is(dictionary):
    winner = ""
    bid = dictionary.values()
    max_bid = max(bid)
    for key, val in dictionary.items():
        if val == max_bid:
           winner = key
    # winner = name[bid.index(max_bid)]
    print(f"The winner is {winner}")

 

    
winner_is(bids)

