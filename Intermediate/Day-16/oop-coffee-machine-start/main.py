from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True






while is_on:
    user_option = input(f"What would you like to drink? Select an option off menu {menu.get_items()}\n")
    if user_option == "off":
        is_on = False
    elif user_option == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_option)
        if coffee_machine.is_resource_sufficient(drink):
            print(f"{drink.name} costs {money_machine.CURRENCY}{drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)