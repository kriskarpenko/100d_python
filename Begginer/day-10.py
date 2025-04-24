# Day 10 - Calculator

first_number = int()
def set_f_num():
    global first_number
    first_number = int(input("What's the first number?"))
operation_type = ''
def set_type():
    global operation_type
    operation_type = input("Choose operation type, type '+', '-', '*' or '/'\n")
second_number = int()
def set_s_num():
    global second_number
    second_number = int(input("What's the second number?"))


def calculate(num_1, oper, num_2):
    """Accepts 2 numbers and a type of operation"""
    result = int()
    another_comand = "yes"
    if another_comand == "yes":
        if oper == "+":
            result = num_1 + num_2
        if oper == "-":
            result = num_1 - num_2
        if oper == "*":
            result = num_1 * num_2
        if oper == "/":
            result = num_1 / num_2
        print(f"Your reault is {result}")
        another_comand = input("Would you like to continue?").lower()
    if another_comand == "no":
        print(f"Great, your result is {result}")

 
set_f_num()
set_type()
set_s_num()
calculate(first_number, operation_type, second_number)