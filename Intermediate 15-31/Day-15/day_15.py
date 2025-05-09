#  Day 15 - coffee machine
from day_15_data import MENU, resources

is_finished = False
is_on = True
u_choice = ""
choice_options = list(MENU.keys())
def machine_button():
    # created to be able to restart the machine after the top up
    global is_finished
    u_choice= input(f"Input Star or Finish to turn on or turn off the coffee machine\n").lower()
    if u_choice == "start":
        is_finished = False
    if u_choice == "finish":
        is_finished = True
def set_u_choice():
    global u_choice
    global is_on
    global is_finished
    u_choice= input(f"What would you like to drink?{choice_options}\n").lower()
    if u_choice == "off":
        is_on = False
    if u_choice == "finish":
        is_finished = True
u_money_set = {'2eu': 0,'1eu': 0, '50c' : 0, '25c' :0 }
u_money = float()
def set_u_money():
    global u_money_set
    global u_money
    u_money_set["2eu"] = int(input("How many €2 are inputting?"))
    u_money_set["1eu"] = int(input("How many €1 are inputting?"))
    u_money_set["50c"] = int(input("How many €0.50 are inputting?"))
    u_money_set["25c"] = int(input("How many €0.25 are inputting?"))
    for key, value in u_money_set.items():
        if key == '2eu':
            u_money += value * 2
        if key == '1eu':
            u_money += value * 1
        if key == '50c':
            u_money += value * 0.5
        if key == '25c':
            u_money += value * 0.25
    print (f"\nYou have put €{u_money}")


resources["money"] = 0 
resources_available = resources["ingredients"]
max_ingridients = {}
for key, value in resources_available.items():
    max_ingridients[key] = value
def top_up():
    print(max_ingridients)
    for key in resources_available:
        resources_available[key] = max_ingridients[key]
        print(key, resources_available[key])
    print("Successfully topped up",resources_available)


machine_button()

while is_on and not is_finished:
        set_u_choice()
        if choice_options.__contains__(u_choice):
            resources_required = MENU[u_choice]['ingredients']
            cost = MENU[u_choice]['cost']

            for ingredient_required, amount_required in resources_required.items():
                amount_available = resources_available[ingredient_required]

                if amount_available < amount_required:
                    print("We're sorry the machine is running low on ingredients. Please choose something else.")
                while amount_available >= amount_required: # while inside of a loop and after all of the ifs so the user only goes to payment step after every ingredient has been checked
                    print(f"{u_choice} costs: {cost}")
                    set_u_money()
                    if u_money >= cost:
                        resources["money"] += cost
                        amount_available -= amount_required
                        resources_available[ingredient_required] = amount_available
                        print(f"You're change is €{u_money - cost}\n")
                    else:
                        print("Sorry that's not enough.")  
                    # breaks in every if state to prevent infinite loop of the same coffee being made
                    break
                break
        elif u_choice == "finish":
            break
        else:
            print("The item you have selected does not exist. Please choose something of menu.")
            break
            
if not is_on and not is_finished:
    print(resources)
    top_up()
    u_choice = input("Would you like to go back to the menu? Print on to go back to menu, or print finish to shut down the machine\n")
    if u_choice == "on":
        is_on = True
    elif u_choice == "finish":
        is_finished = True

if is_finished:
    print("Tank you for checking out the machine, see you soon")



# Task:
#     1. Check if the machine is on, by default - yes
#     2. User decides which coffee they want
#     3. Check if the resources are sufficient
#     4. Ask user for coins
#     5. If amount of coins is sufficient make coffee, reduce the used resources
#     6. if the machine is off, print report on resources, add a restore option

# Thought process:
#  Machine has been checked, moving onto calculating  user's money
#  Made a money key in the resources dictionary. Now checking if the required amount of resources is available
#  Resolving an issue of how to top up the ingredients when they ran out 
#  thought: what if i create a duplicate of an ingredients dict at the beginning of the code and then on a top up function i reassign the values of the ingredient dict with the values of duplicate dict
#  Ran into a problem of only one ingredient being checked, resolved by adding a while loop after all of the if statements inside of for required_ingredients loop have been ran. 
#  Actually fixed by adding break after every step in first if in the while is on and not finished loop
#  Created is_finished var and a machine button fun to be able to continue running machine after top up

