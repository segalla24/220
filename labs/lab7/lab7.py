"""
Name: Logan Segal
lab 7.py

Problem: In this lab we practiced working with parameters and conditionals.
    We created different functions doing a specific movement, then we brought all
    together at the end of our code to create one huge movement.

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from random import randint
import math
from graphics import GraphWin, color_rgb, Point, Circle


def get_random(move_amount):
    random = randint(-move_amount, move_amount)
    return random


def did_collide(cb, cb2):
    center_1 = cb.getCenter()
    center_2 = cb2.getCenter()
    c1x = center_1.getX()
    c1y = center_1.getY()
    c2x = center_2.getX()
    c2y = center_2.getY()

    x_equation = (c2x - c1x) ** 2
    y_equation = (c2y - c1y) ** 2
    distance = math.sqrt(x_equation + y_equation)

    radius_1 = cb.getRadius()
    radius_2 = cb2.getRadius()
    radii_sum = radius_2 + radius_1

    if distance <= radii_sum:
        return True
    else:
        return False


def hit_vertical(cb, win):
    v_center = cb.getCenter()
    v_center_x = v_center.getY()
    v_radius = cb.getRadius()
    v_height = win.getHeight()
    return v_center_x <= v_radius or v_center_x >= v_height - v_radius


def hit_horizontal(cb, win):
    h_center = cb.getCenter()
    h_center_x = h_center.getX()
    h_radius = cb.getRadius()
    h_width = win.getWidth()
    return h_center_x <= h_radius or h_center_x >= h_width - h_radius


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    colors = color_rgb(red, green, blue)
    return colors


def bumper():
    win = GraphWin("bumper", 400, 400)
    circ1 = Circle(Point(randint(1, 400), randint(1, 400)), 30)
    circ1.setFill(get_random_color())
    circ1.draw(win)
    circ2 = Circle(Point(randint(1, 400), randint(1, 400)), 30)
    circ2.setFill(get_random_color())
    circ2.draw(win)

    circ1_x_move = get_random(25)
    circ1_y_move = get_random(25)
    circ2_x_move = get_random(25)
    circ2_y_move = get_random(25)

    while not win.checkMouse():
        circ1.move(circ1_x_move, circ1_y_move)
        circ2.move(circ2_x_move, circ2_y_move)
        if did_collide(circ1, circ2):
            circ1_x_move = -circ1_x_move
            circ1_y_move = -circ1_y_move
            circ2_x_move = -circ2_x_move
            circ2_y_move = -circ2_y_move
        if hit_horizontal(circ1, win):
            circ1_x_move = -circ1_x_move
        if hit_horizontal(circ2, win):
            circ2_x_move = -circ2_x_move
        if hit_vertical(circ1, win):
            circ1_y_move = -circ1_y_move
        if hit_vertical(circ2, win):
            circ2_y_move = -circ2_y_move

    win.close()
bumper()