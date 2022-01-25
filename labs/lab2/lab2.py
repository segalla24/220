"""
Name: Logan Segal
Lab 2.py

Problem: In this lab we used loops in order to find different means. We were also introduced to accumulators which helped
us create/find these means. We practiced using basic math functions in python and learning how to use 'shortcuts' to help us

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def means():
    values = eval(input("How many values do you want to enter?"))
    rms_acc = 0
    h_acc = 0
    g_acc = 1
    for i in range(values):
        value_amount = eval(input("enter value: "))
        rms_acc = rms_acc + value_amount ** 2
        h_acc = 1 / value_amount + h_acc
        g_acc = value_amount * g_acc
    rms_acc = rms_acc / values
    rms = rms_acc ** 0.5
    harm = values / h_acc
    geo = g_acc ** (1/values)
    print("RMS is: ", rms)
    print("Harmonic is: ", harm)
    print("Geometric is: ", geo)

means()









