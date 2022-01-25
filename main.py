# Course: CS 30
# Period: 3
# Date created: December 25th, 2021
# Date modified: January 23th, 2022
# Name: Zana Osman
# Description: Mainfile for the program
try:
    import sys
    import income as inc
    import expense as exp
except ModuleNotFoundError:
    print("Module not imported correctly, Main")
    sys.exit()

# This is the print statement for the starting option
starting_option = ("[1] File Income!", "[2] File Expense!",
                   "[3] Check Total Balance", "[4] Quit")
income_choice = ("[1] File income", "[2] Check filed income")


def check_positive():
    total_i_e = inc.total_income() - exp.total_expense()
    if total_i_e < 1:
        print("\033[1;32;40m Bright Green  \n")
    elif total_i_e > 1:
        print("\033[1;31;40m Red  \n")


while True:
    """Function for the menu"""
    for choices in starting_option:
        print(f"\n{choices}")
    menuchoice = str(input("\n>"))
    if menuchoice == "1":
        for choices in income_choice:
            print(f"\n{choices}")
            income_option = input("\n>")
            if income_option == "1":
                inc.Add_income()
            elif income_option == "2":
                inc.income_checker()
    elif menuchoice == "2":
        print("Lol")
    elif menuchoice == "3":
        print("Balance:")
        check_positive()
    elif menuchoice == "4":
        if menuchoice == "4":
            choice_s = str(
                input("\nAre you sure you would like to exit? [Y] "))
            if choice_s == "Y":
                print("Exiting, Goodbye")
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("\nSorry that does not work, Choose a different option\n")
