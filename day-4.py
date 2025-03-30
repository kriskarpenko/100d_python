#Day 4 - rock, paper, scissors

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# indx = random.randint(0,4)

# print(friends[indx])
# print(random.choice(friends))



import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = [rock, paper, scissors]
computer_choice = random.choice(option)

usr_choice = option[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]
print(usr_choice, "Computer chose:",computer_choice)
# If user chooses Rock
if usr_choice == rock and computer_choice == scissors:
    print("You won")
elif usr_choice == rock and computer_choice == rock:
    print("It's a draw")
elif usr_choice == rock and computer_choice == paper:
    print("You loose")

# If user chooses Paper
if usr_choice == paper and computer_choice == rock:
    print("You won")
elif usr_choice == paper and computer_choice == paper:
    print("It's a draw")
elif usr_choice == paper and computer_choice == scissors:
    print("You loose")

# If user chooses Scissors
if usr_choice == scissors and computer_choice == paper:
    print("You won")
elif usr_choice == scissors and computer_choice == scissors:
    print("It's a draw")
elif usr_choice == scissors and computer_choice == rock:
    print("You loose")