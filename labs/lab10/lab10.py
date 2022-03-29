"""
Name: Logan Segal
lab 10.py

Problem: In this lab we are working with creating our own classes to create a
    program. Once we have created our classes we imported them to our main document
    and utilized them to make a functional program. We combined our new knowledge of
    classes with our previous knowledge of graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Rectangle, Point
from button import Button
from door import Door


def main():
    win = GraphWin("Test", 700, 700)
    exit = Button(Rectangle(Point(200,50),Point(500,200)), "Exit")
    exit.color_button("light gray")
    exit.draw(win)

    door = Door(Rectangle(Point(200, 250), Point(500, 680)), "Closed")
    door.color_door("red")
    door.draw(win)

    point = win.getMouse()
    while not exit.is_clicked(point):
        if door.is_clicked(point) and door.get_label() == "Open":
            door.close("red", "Closed")
        else:
            door.open("white", "Open")
        point = win.getMouse()

    win.close()

main()