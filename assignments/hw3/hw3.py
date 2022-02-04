"""
Name: Logan Segal
Homework 3.py

Problem: For this homework we worked with creating functions with for loops to help solve
different problems. We also worked with incorporating formulas in our code to help solve math
problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    g_amount = eval(input("how many grades would you like to enter? "))
    total_grades = 0
    for i in range(g_amount):
        grades = eval(input("enter grade: "))
        total_grades = total_grades + grades
    avg = total_grades / g_amount
    print("average is:", avg)


def tip_jar():
    total_tips = 0
    for i in range(5):
        tip = eval(input("how much would you like to donate? "))
        total_tips = total_tips + tip
    print("total tips:", total_tips)


def newton():
    sqr_root = eval(input("what number do you want to square root? "))
    times = eval(input("how many times should we improve the approximation? "))
    approx = sqr_root
    for i in range(times):
        approx = (approx + (sqr_root / approx)) / 2
    print("the square root is approximately", approx)


def sequence():
    terms = eval(input("how many terms would you like? "))
    for i in range(1, terms+1):
        print((i-1) + (i % 2), end="\t")


def pi():
    t_in_s = eval(input("how many terms in the series? "))
    approx = 1
    for i in range(t_in_s):
        n_rator = (2 + (i//2) * 2)
        d_nator = (1 + ((i+1)//2) * 2)
        div = n_rator / d_nator
        approx = approx * div
        result = approx * 2
    print(result)


if __name__ == '__main__':
    average()
    tip_jar()
    newton()
    sequence()
    pi()
