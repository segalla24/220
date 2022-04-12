"""
Name: Logan Segal
lab 12.py

Problem: In this lab we are working with list manipulations and while loops. In this lab we
    weren't able to use either 'breaks' or for loops. Our end goal for this lab was to create
    a successful high and low game, and we did this with the help of our previous created functions.
    In this lab we used previous and


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            list.insert(i, "Logan")
            list.pop(i + 1)
        i += 1


def good_input():
    num = 0
    while num < 1 or num > 10:
        num = eval(input("guess a number: "))
        if num > 10:
            print("too high")
        elif num < 1:
            print("too low")


def num_digits():
    num = eval(input("enter a positive integer [OR enter a negative number or zero to quit]: "))
    while num > 1:
        count = 0
        place_holder = num
        while place_holder != 0:
            count = count + 1
            place_holder = place_holder // 10
        print(count)
        num = eval(input("enter a positive integer [OR enter a negative number or zero to quit]: "))


def hi_lo_game():
    random = randint(1, 100)
    tries = 1
    guess = eval(input("guess a number: "))
    while guess != random and tries and guess != 7:
        tries = tries + 1
        if guess < random:
            print("too low")
        else:
            print("too high")
        guess = eval(input("guess a number: "))
        if tries == 7:
            print("sorry you lose. the number was " + str(random))
        elif guess == random:
            print("you won in " + str(tries) + " guesses!")

