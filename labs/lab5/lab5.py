"""
Name: Logan Segal
Lab 5.py

Problem: In this lab we got more practice using the graphics library. We combined
    this with what we have learned so far in python with loops and arithmatic math.
    However, we also worked on problems that had to do with strings and lists by
    producing different outputs using the same input.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Point, Text, Polygon, Circle, Entry, color_rgb
import math


def triangle():
    win = GraphWin("Triangle", 400, 400)

    instructions = Text(Point(175, 100), "click 3 times (in different areas) on the screen")
    instructions.draw(win)

    click1 = win.getMouse()
    click1x = click1.getX()
    click1y = click1.getY()

    click2 = win.getMouse()
    click2x = click2.getX()
    click2y = click2.getY()

    click3 = win.getMouse()
    click3x = click3.getX()
    click3y = click3.getY()

    shape = Polygon(Point(click1x, click1y), Point(click2x, click2y), Point(click3x, click3y))
    shape.setOutline("black")
    shape.setFill("blue")
    shape.draw(win)

    sl1x = click2x - click1x
    sl1y = click2y - click1y

    sl2x = click3x - click2x
    sl2y = click3y - click2y

    sl3x = click1x - click3x
    sl3y = click1y - click3y

    side_a = math.sqrt((sl1x**2)+(sl1y**2))
    side_b = math.sqrt((sl2x**2)+(sl2y**2))
    side_c = math.sqrt((sl3x**2)+(sl3y**2))
    side = ((side_a + side_b + side_c)/2)

    perimeter = (side_a + side_b + side_c)
    per_txt = "Perimeter:", perimeter
    p_label = Text(Point(200, 325), per_txt)
    p_label.draw(win)

    area_info = side * (side - side_a) * (side - side_b) * (side - side_c)
    area = math.sqrt(area_info)
    a_txt = "Area:", area
    a_label = Text(Point(200, 350), a_txt)
    a_label.draw(win)

    f_struct = Text(Point(200, 200), "click again to close")
    f_struct.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)
    # shape.setFill(color_rgb(red, green, blue))

    # redTexPt is 50 pixels to the left and forty pixels down from center

    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_entry = Entry(Point(210, 240), 10)
    red_entry.draw(win)
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_entry = Entry(Point(210, 270), 10)
    green_entry.draw(win)
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_entry = Entry(Point(210, 300), 10)
    blue_entry.draw(win)
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red_gt = red_entry.getText()
        r_fill = eval(red_gt)
        blue_gt = blue_entry.getText()
        b_fill = eval(blue_gt)
        green_gt = green_entry.getText()
        g_fill = eval(green_gt)
        shape.setFill(color_rgb(r_fill, g_fill, b_fill))

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    text = input("enter a string to process: ")
    first_chr = text[0]
    print(first_chr)
    last_chr = text[-1]
    print(last_chr)
    mid_chr = text[1:5]
    print(mid_chr)
    f_and_l = text[0] + text[-1]
    print(f_and_l)
    repeat = text[0:3] * 10
    print(repeat)
    for i in text:
        print(i)
    length = len(text)
    print(length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[-1])]
    print(x)
    x = values[2] + values[0] + float(values[-1])
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("how many terms? "))
    acc = 0
    for i in range(terms):
        seq = 2 + 2*(i % 3)
        print(seq, end=" ")
        acc = acc + seq
    print("\n", "sum =", acc)


def target():
    win = GraphWin("Target", 400, 400)
    win.setBackground("light gray")

    white = Circle(Point(200, 200), 200)
    white.setOutline("white")
    white.setFill("white")
    white.draw(win)

    black = Circle(Point(200, 200), 160)
    black.setOutline("black")
    black.setFill("black")
    black.draw(win)

    blue = Circle(Point(200, 200), 120)
    blue.setOutline("blue")
    blue.setFill("blue")
    blue.draw(win)

    red = Circle(Point(200, 200), 80)
    red.setOutline("red")
    red.setFill("red")
    red.draw(win)

    yellow = Circle(Point(200, 200), 40)
    yellow.setOutline("yellow")
    yellow.setFill("yellow")
    yellow.draw(win)

    f_struct = Text(Point(200, 200), "click again to close")
    f_struct.draw(win)
    win.getMouse()
    win.close()



