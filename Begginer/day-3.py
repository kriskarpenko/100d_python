#Day 3 - pizza maker

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# Determining the price based on the size of pizza
if size == "S":
    bill = 15
    # if pepperoni == "Y":
    #     bill +=2
elif size == "M":
    bill = 20
    # if pepperoni == "Y":
    #     bill +=3
else:
    bill = 25
    # if pepperoni == "Y":
    #     bill +=3
# extra cheese
if extra_cheese == "Y":
    bill +=1
# extra pepperoni
if pepperoni == "Y" and size == "S":
    bill +=2
elif pepperoni == "Y":
    bill += 3
print(f"Your final bill is: ${bill}.")