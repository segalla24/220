"""
Name: Logan Segal
homework 6.py

Problem: In this homework we will be working with more strings and adding
    parameters to our functions. In this homework we will be dealing with
    arguments, formatting, encoding, and decoding. However, now we are adding on
    to our previous knowledge while also combining it with topics we have learned
    in the past.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    integer = float(input("enter an integer "))
    print("that is ${:.2f}".format(integer))


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    len_msg = len(message)
    my_string = ""
    for i in range(len_msg):
        msg_num = ord(message[i])
        total = msg_num + key
        revert = chr(total)
        my_string = my_string + revert
    print(my_string)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    total = number * (number + 1) / 2
    return total


def sum_n_cubes(number):
    cubes = (number * (number + 1) / 2) ** 2
    return cubes


def encode_better():
    message = input("enter a message: ")
    key = input("enter a key: ")
    len_msg = len(message)
    my_string = ""
    for i in range(len_msg):
        msg_num = ord(message[i]) - 65
        key_num = ord(key[i % len(key)]) - 65
        total = msg_num + key_num
        mod = total % 58
        convert = mod + 65
        revert = chr(convert)
        my_string = my_string + revert
    print(my_string)


if __name__ == '__main__':
    cash_converter()
    encode()
    res = sphere_area(13)
    print(res)
    res = sphere_volume(13)
    print(res)
    res = sum_n(100)
    print(res)
    res = sum_n_cubes(13)
    print(res)
    encode_better()
