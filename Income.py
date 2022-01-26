# Course: CS 30
# Period: 3
# Date created: December 25th, 2021
# Date modified: January 25th, 2022
# Name: Zana Osman
# Description: income for the program
global clear_console

i1 = []
i2 = []
i3 = []


def file_choice_inc():
    '''Takes income from the user'''
    ask_which = input("File entry 1, 2 or 3\n>")
    if ask_which == "1":
        amount1 = int(input("How much have you made today?"))
        if amount1 > 0:
            i1.append(amount1)
    elif ask_which == "2":
        amount2 = int(input("How much have you made today?"))
        if amount2 > 0:
            i2.append(amount2)
    elif ask_which == "3":
        amount3 = int(input("How much have you made today?"))
        if amount3 > 0:
            i3.append(amount3)


amount1 = i1
amount2 = i2
amount3 = i3


def see_income():
    '''Checks to see all the income that user has added'''
    chosen_to_check = input(
        str("Which entry would you like to see? [1, 2, 3]\n>"))
    global amount1, amount2, amount3
    if chosen_to_check == "1":
        print(amount1)
    elif chosen_to_check == "2":
        print(amount2)
    elif chosen_to_check == "3":
        print(amount3)


def total_income():
    '''Adds all the income into one'''
    global amount1, amount2, amount3
    sum = amount1 + amount2 + amount3
    print(sum)


def total_income_balance():
    '''Adds all the income into one for final count'''
    global amount1, amount2, amount3
    total_inc_sum = sum(i1 + i2 + i3)
    print(total_inc_sum)
