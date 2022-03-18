"""
Name: Logan Segal
Homework 8.py

Problem: In this homework we practiced working with parameters and conditionals,
    specifically conditional control structures. We combined this knowledge with
    previous knowledge and topics we have learned in the past to complete this
    homework.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin, Circle, Text, Point


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    num_sum = sum(nums)
    return num_sum


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    my_list = []
    for i in range(len(nums)):
        num_split = nums[i].split(", ")
        to_numbers(num_split)
        square_each(num_split)
        value = sum_list(num_split)
        my_list.append(value)
    return my_list


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 400 == 0 or year % 100 and year % 4 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference2.getX()) ** 2 + (center2.getY() - circumference2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    true_msg = Text(Point(5, 4), "The circles overlap.")
    false_msg = Text(Point(5, 4), "The circles do not overlap.")
    close_msg = Text(Point(5, 3), "Click again to close.")

    if did_overlap(circle_one, circle_two):
        true_msg.draw(win)
        close_msg.draw(win)
    else:
        false_msg.draw(win)
        close_msg.draw(win)

    win.getMouse()

circle_overlap()

def did_overlap(circle_one, circle_two):
    center_1 = circle_one.getCenter()
    center_2 = circle_two.getCenter()
    c1x = center_1.getX()
    c1y = center_1.getY()
    c2x = center_2.getX()
    c2y = center_2.getY()

    x_equation = (c2x - c1x) ** 2
    y_equation = (c2y - c1y) ** 2
    distance = math.sqrt(x_equation + y_equation)

    radius_1 = circle_one.getRadius()
    radius_2 = circle_two.getRadius()
    radii_sum = radius_2 + radius_1

    if distance <= radii_sum:
        print("The circles overlap.")
        return True
    else:
        print("The circles do not overlap.")
        return False
did_overlap()

if __name__ == '__main__':
    pass
