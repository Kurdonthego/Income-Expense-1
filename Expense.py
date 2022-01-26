# Course: CS 30
# Period: 3
# Date created: December 25th, 2021
# Date modified: January 25th, 2022
# Name: Zana Osman
# Description: Expense for the program
global clear_console

e1 = []
e2 = []
e3 = []


def file_choice_exp():
    '''Takes expense from the user'''
    ask_which = input("File entry 1, 2 or 3\n>")
    if ask_which == "1":
        e_amount1 = int(input("How much have you made today?"))
        if e_amount1 > 0:
            e1.append(e_amount1)
    elif ask_which == "2":
        e_amount2 = int(input("How much have you made today?\n> "))
        if e_amount2 > 0:
            e2.append(e_amount2)
    elif ask_which == "3":
        e_amount3 = int(input("How much have you made today?\n> "))
        if e_amount3 > 0:
            e3.append(e_amount3)


e_amount1 = e1
e_amount2 = e2
e_amount3 = e3


def see_expense():
    '''Checks to see all the expenses that user has added'''
    chosen_to_check = input(
        str("Which entry would you like to see? [1, 2, 3]\n>"))
    global e_amount1, e_amount2, e_amount3
    if chosen_to_check == "1":
        print(e_amount1)
    elif chosen_to_check == "2":
        print(e_amount2)
    elif chosen_to_check == "3":
        print(e_amount3)


def total_expense():
    '''Adds all the expenses into one'''
    global e_amount1, e_amount2, e_amount3
    sum = e_amount1 + e_amount2 + e_amount3
    print(sum)


def total_expense_balance():
    '''Adds all the expenses into one for final count'''
    global e_amount1, e_amount2, e_amount3
    total_exp_sum = sum(e1 + e2 + e3)
    print(total_exp_sum)
