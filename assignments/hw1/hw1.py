"""
Name: Logan Segal
segal-homework 1.py

Problem: In this homework I was able to get more comfortable with python and using simple functions. I was able to create
    functions that can help me do simple problems by collecting data

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the players total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooting_ratio = shots_made / total_shots
    shooting_percentage = shooting_ratio * 100
    print("Shooting Percentage= ", shooting_percentage)


def coffee():
    coffee_amount = eval(input("How many pounds of coffee would you like?"))
    coffee_cost = 10.50
    shipping_cost = 0.86
    fixed_cost = 1.50
    total = coffee_amount * coffee_cost + coffee_amount * shipping_cost + fixed_cost
    print("Your total is:", total)


def kilometers_to_miles():
    kilometer = eval(input("How many kilometers did you travel?"))
    mile = kilometer * 0.621371
    round_mile = round(mile,1)
    print("That's",round_mile,"miles!")



if __name__ == '__main__':
    pass
