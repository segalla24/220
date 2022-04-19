"""
Name: Logan Segal
lab 13.py

Problem: In this lab we worked with search and sort algorithms. We took data and problems
    and coded functions that relate more to real world issues. In this lab we used all
    the knowledge we have learned in Python!


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


def selection_sort(values):
    for i in range(len(values)):
        minimum = i
        for j in range(i+1, len(values)):
            if values[minimum] > values[j]:
                minimum = j
        values[i], values[minimum] = values[minimum], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p1x = p1.getX()
    p1y = p1.getY()
    p2 = rect.getP2()
    p2x = p2.getX()
    p2y = p2.getY()
    width = p2x - p1x
    height = p2y - p1y
    area = width * height
    return area


def rect_sort(rectangles):
    my_list = []
    for i in rectangles:
        individual = calc_area(i)
        my_list.append(individual)
        for j in range(len(my_list)):
            index = j
            smallest_area = my_list[j]
            for k in range(j+1, len(my_list)):
                if my_list[k] < smallest_area:
                    smallest_area = my_list[k]
                    index = k
            my_list[j], my_list[index] = my_list[index], my_list[i]





