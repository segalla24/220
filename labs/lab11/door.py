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
from graphics import Text


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        xxx = point.getX()
        yyy = point.getY()
        rectp1 = self.shape.getP1()
        rectp2 = self.shape.getP2()
        r1x = rectp1.getX()
        r1y = rectp1.getY()
        r2x = rectp2.getX()
        r2y = rectp2.getY()
        if r2x >= xxx >= r1x and r2y >= yyy >= r1y:
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color,label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self,color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret
