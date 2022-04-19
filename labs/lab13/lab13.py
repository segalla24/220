"""
Name: Logan Segal
lab 13.py

Problem: In this lab we worked with search and sort algorithms. We took data and problems
    and coded functions that relate more to real world issues. In this lab we used all
    the knowledge we have learned in Python!


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    infile = open(filename, 'r')
    line = infile.read()
    numbers = line.split()
    for i in range(len(numbers)):
        if eval(numbers[i]) > 830:
            time_stamp = i + 1
            print("WARNING! there are more than 830 trades!")
            print("more than 830 trades happened at ", time_stamp, " seconds")
        elif eval(numbers[i]) == 500:
            timestamp = i + 1
            print("ALERT! there are exactly 500 trades!")
            print("exactly 500 trades happened at ", timestamp, " seconds")
    infile.close()





