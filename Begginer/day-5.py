#Day 5 - password randomiser

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
smbl_total = nr_symbols + nr_letters +nr_numbers

# Easy
# password = ''
#
# for char in range (0, nr_letters):
#     password += rand_letter
# for char in range (0, nr_symbols):
#     password += random_symb
# for char in range (0, nr_numbers):
#     password += rand_numb


password_list= []
for char in range (0, nr_letters):
    (password_list.append(random.choice(letters)))
for char in range (0, nr_symbols):
    (password_list.append(random.choice(symbols)))
for char in range (0, nr_numbers):
    (password_list.append(random.choice(numbers)))
random.shuffle(password_list)

password=''
for char in password_list:
    password += char
print(password)