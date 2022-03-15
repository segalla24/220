"""
Name: Logan Segal
lab 8.py

Problem: In this lab we worked with opening and editing files. We combined our
    knowledge of files with the previous topics we have learned so far in the class.
    To complete the lab, we primarily worked with strings, loops, and averages to output
    a new file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    avg = open(out_file_name, 'w')
    info = in_file.readlines()
    total = 0
    num_perf = 0
    for line in info:
        split_line = line.split(':')
        names = split_line[0]
        numbers = split_line[1].strip().split()
        weight = 0
        add = 0
        for i in range(0, len(numbers), 2):
            weight = eval(numbers[i]) + weight
            student_mult = eval(numbers[i]) * eval(numbers[i+1])
            add = add + student_mult
        rnd_student_average = round(add/100, 1)
        if weight > 100:
            avg.write(names + "'s average: Error: The weights are more than 100." + "\n")
        elif weight < 100:
            avg.write(names + "'s average: Error: The weights are more than 100." + "\n")
        else:
            total = total + rnd_student_average
            num_perf = num_perf + 1
            avg.write(names + "'s average: " + str(rnd_student_average) + "\n")
    class_avg = total / num_perf
    avg.write("Class average: " + str(class_avg))

    in_file.close()
    avg.close()


weighted_average("grades.txt", "avg.txt")
