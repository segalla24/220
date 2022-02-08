"""
Name: Logan Segal
Lab 4.py

Problem: In this lab we are working with graphics built in library to create a Valentine's Day card.
    We are having practice using different drawing shapes, working with text, and combining this with animation
    and loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import graphics
import time

def greeting_card():
    win = graphics.GraphWin("Valentine's Day", 700, 700)
    win.setBackground("pink")

    left_circ = graphics.Circle(graphics.Point(270, 230), 75)
    left_circ.setFill("white")
    left_circ.setOutline("white")
    left_circ.draw(win)

    middle_circ = graphics.Circle(graphics.Point(330,300),40)
    middle_circ.setFill("white")
    middle_circ.setOutline("white")
    middle_circ.draw(win)

    right_circ = graphics.Circle(graphics.Point(410, 230), 75)
    right_circ.setFill("white")
    right_circ.setOutline("white")
    right_circ.draw(win)

    tri = graphics.Polygon(graphics.Point(205, 270), graphics.Point(475, 270), graphics.Point(340, 400))
    tri.setFill("white")
    tri.setOutline("white")
    tri.draw(win)

    a_line = graphics.Line(graphics.Point(0, 500), graphics.Point(100, 425))
    a_line.setWidth(5)
    a_line.setArrow("last")
    a_line.draw(win)

    label = graphics.Text(graphics.Point(350, 500), "Happy Valentine's Day!!!")
    label.setSize(30)
    label.setTextColor("red")
    label.draw(win)

    for i in range(7):
        a_line.move(100, -50)
        time.sleep(0.5)

    f_mess = graphics.Text(graphics.Point(350, 600), "click anywhere to close")
    f_mess.setSize(18)
    f_mess.draw(win)

    win.getMouse()
    win.close()

greeting_card()