"""
Name: Logan Segal
segal-homework 2.py

Problem: <For the homework we practiced using the import math library with different functions. We also had practice
 working with loops and accumulators>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    up_bound = eval(input("what is the upper bound?"))
    sum = 0
    for i in range(0, up_bound+1, 3):
        sum = sum + i
    print("sum of threes is", sum)


def multiplication_table():
   for i in range(1,11):
       for j in range(1,11):
            print(i*j, end="\t")
       print()


def triangle_area():
    side_a = eval(input("enter side a length: "))
    side_b = eval(input("enter side b length:"))
    side_c = eval(input("enter side c length: "))
    s_perm = (side_a + side_b + side_c)/2
    s_minus_a = s_perm - side_a
    s_minus_b = s_perm - side_b
    s_minus_c = s_perm - side_c
    area = math.sqrt(s_perm*s_minus_a*s_minus_b*s_minus_c)
    round_area = round(area, 2)
    print("the area is", round_area)


def sum_squares():
    lo_range = eval(input("enter the lower range: "))
    up_range = eval(input("enter the upper range: "))
    sum= 0
    for i in range(lo_range, up_range+1, 1):
        sum = sum + math.pow(i, 2)
    print(sum)


def power():
    base = eval(input("enter the base: "))
    exponent = eval(input("enter the exponent: "))
    power = 1
    for i in range(1, exponent+1):
        power = power * base
    print(base, "^", exponent, "=", power)


if __name__ == '__main__':
    sum_of_threes()
    multiplication_table()
    triangle_area()
    sum_squares()
    power()
