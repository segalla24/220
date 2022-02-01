"""
Name: Logan Segal
Lab 3.py

Problem: For this lab we worked with loops and finding the averages and totals given a real life situation. We practiced
our skills and previous knowledge but also learned how to reset a loop, which we used to find the average of each
specific road.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    roads = eval(input("How many roads were surveyed?"))
    sum = 0
    for i in range(roads):
        spec_sum = 0
        print("How many days was road", i+1, "surveyed?")
        days = eval(input(""))
        for j in range(days):
            print("\tHow many cars traveled on day", j+1, "?")
            cars = eval(input(""))
            sum = sum + cars
            spec_sum = spec_sum + cars
        spec_avg = spec_sum / days
        print("Road", i+1, "average vehicles per day:", spec_avg)
    avg = sum / roads
    rnd_avg = round(avg, 2)
    print("Total number of vehicles traveled on all roads:", sum)
    print("Average number of vehicles per road:", rnd_avg)


traffic()
