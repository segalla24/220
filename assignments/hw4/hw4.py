"""
Name: Logan Segal
homework 4.py

Problem: For this homework we practiced working with the graphics library.
    We combined this with math problems, by creating shapes and creating a code
    that would help find the area/perimeter/radius based on the users clicks.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import Point, GraphWin, Circle, Rectangle, Text


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "click to draw square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle
        copy = shape.clone()
        copy.draw(win)

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

    f_struct = Text(Point(200, 200), "click again to close")
    f_struct.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)

    click1 = win.getMouse()
    click1x = click1.getX()
    click1y = click1.getY()
    click2 = win.getMouse()
    click2x = click2.getX()
    click2y = click2.getY()

    shape = Rectangle(Point(click1x, click1y), Point(click2x, click2y))
    shape.setOutline("black")
    shape.setFill("green")
    shape.draw(win)

    perimeter = 2 * (click2x + click2y)
    per_txt = "Perimeter:", perimeter
    p_label = Text(Point(200, 325), per_txt)
    p_label.draw(win)

    area = (click1x - click2x) * (click1y - click2y)
    a_txt = "Area:", area
    a_label = Text(Point(200, 350), a_txt)
    a_label.draw(win)

    f_struct = Text(Point(200, 200), "click again to close")
    f_struct.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)

    click1 = win.getMouse()
    click1x = click1.getX()
    click1y = click1.getY()
    c_point = Point(click1x, click1y)
    click2 = win.getMouse()
    click2x = click2.getX()
    click2y = click2.getY()

    dist_form = math.sqrt(((click2x - click1x) ** 2)+((click2y - click1y) ** 2))
    shape = Circle(c_point, dist_form)
    shape.setOutline("black")
    shape.setFill("light blue")
    rds = "Radius:", dist_form
    label = Text(Point(200, 350), rds)
    shape.draw(win)
    label.draw(win)

    f_struct = Text(Point(200, 200), "click again to close")
    f_struct.draw(win)
    win.getMouse()
    win.close()


def pi2():
    num_term = eval(input("enter the number of terms to sum: "))
    approx = 0
    denom = 1
    switch = 1
    for i in range(num_term):
        approx = approx + switch * (4 / denom)
        denom = denom + 2
        switch = switch * -1
    accuracy = abs(math.pi - approx)
    print("pi approximation:", approx)
    print("accuracy:", accuracy)


if __name__ == '__main__':
    squares()
    rectangle()
    circle()
    pi2()
