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


def read_data(file_name):
    i = 0
    my_list = []
    my_file = open(file_name, "r")
    lines = my_file.read()
    words = lines.split()
    while i < len(words):
        value = eval(words[i])
        my_list.append(value)
        i = i + 1
    my_file.close()
    return my_list


def is_in_linear(search_value, values):
    i = 0
    while i < len(values):
        if search_value in values:
            return True
        else:
            return False








