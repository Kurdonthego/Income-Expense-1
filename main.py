# Course: CS 30
# Period: 3
# Date created: December 25th, 2021
# Date modified: January 23th, 2022
# Name: Zana Osman
# Description: Mainfile for the program
try:
    import sys
    import os
    import income as inc
    import expense as exp
except ModuleNotFoundError:
    print("Module not imported correctly, Main")
    sys.exit()

# This is the print statement for the starting option
starting_option = ("[1] File Income!", "[2] File Expense!",
                   "[3] Check Total Balance", "[4] Quit")

# These are the choices the user will have when they choose income
income_choice = ("[1] File income", "[2] Check filed income")

# These are the choices the user will have when they choose expense
expense_choice = ("[1] File expense", "[2] Check filed expense")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def check_positive():
    '''Checks to see if the total is positive or negative'''
    a = inc.total_income()
    b = exp.total_expense()
    total_i_e = a - b
    if total_i_e < 1:
        print("\033[1;32;40m Bright Green  \n")
    elif total_i_e > 1:
        print("\033[1;31;40m Red  \n")


while True:
    """Function for the menu"""
    for choices in starting_option:
        print(f"\n{choices}")
    menuchoice = str(input("\n>"))
    clearConsole()
    if menuchoice == "1":
        for choices in income_choice:
            print(f"\n{choices}")
        income_option = input("\n>")
        if income_option == "1":
            clearConsole()
            inc.file_choice_inc()
        elif income_option == "2":
            clearConsole()
            inc.total_income()
    elif menuchoice == "2":
        for choices in expense_choice:
            print(f"\n{choices}")
        expense_option = input("\n>")
        if expense_option == "1":
            clearConsole()
            exp.file_choice_exp()
        elif expense_option == "2":
            clearConsole()
            exp.total_expense()
    elif menuchoice == "3":
        clearConsole()
        print("Balance:")
        check_positive()
    elif menuchoice == "4":
        if menuchoice == "4":
            clearConsole()
            choice_s = str(
                input("\nAre you sure you would like to exit? [Y] "))
            if choice_s == "Y":
                clearConsole()
                print("Exiting, Goodbye")
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("\nSorry that does not work, Choose a different option\n")
