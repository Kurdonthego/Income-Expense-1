# Course: CS 30
# Period: 3
# Date created: December 25th, 2021
# Date modified: January 23th, 2022
# Name: Zana Osman
# Description: income for the program

i1 = []
i2 = []
i3 = []

current_inc = i1

income = 0


def income_checker():
    """Checks to see which income statement is empty"""
    global current_inc
    if income == 1:
        current_inc = i1
    elif income == 2:
        current_inc = i2
    elif income == 3:
        current_inc = i3


def Add_income():
    global income
    income_checker()
    amount = input(str("How much have you made today?"))
    if amount > 0:
        income += 1
        i1.append()


def see_income():
    print(i1)
    print(i2)
    print(i3)


def total_income():
    sum = i1 + i2 + i3
    print("sum:", sum)


def reset_income():
    """Resets all income statements made"""
    global current_inc
    global income
    income -= 1
    while income > 1:
        income_checker
        current_inc.clear()
        income -= 1
    income += 1
