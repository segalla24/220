"""
Name: Logan Segal
Homework 10.py

Problem: In this homework we are working with creating our own classes and functions.
    We created everything from a blank coding page, and coded everything ourselves
    from start to finish. This homework utilizes everything we have learned so far, with
    the new topics we have learned about creating our own classes.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Circle, Line,Polygon


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        middle = self.head.getCenter()
        radius = self.head.getRadius()
        size = 0.8 * radius
        mouth = radius / 2.0
        point_3 = middle.clone()
        point_3.move(0, mouth * 1.0)
        point_1 = middle.clone()
        point_1.move(-size / 2, mouth)
        point_2 = middle.clone()
        point_2.move(size / 2, mouth)
        self.mouth.undraw()
        self.mouth = Polygon(point_1, point_2, point_3)
        self.mouth.draw(self.window)

    def shock(self):
        radius = self.head.getRadius()
        size = 0.20 * radius
        center = self.mouth.getCenter()
        shock_expression = Circle(center, size)
        self.mouth.undraw()
        self.mouth = shock_expression
        self.mouth.draw(self.window)

    def wink(self):
        middle = self.head.getCenter()
        radius = self.head.getRadius()
        eye_close = radius / 3.0
        point_1 = middle.clone()
        point_1.move(-eye_close / 1.6, - eye_close)
        point_2 = middle.clone()
        point_2.move(eye_close / 2, - eye_close)
        eye_wink = Line(point_1, point_2)
        eye_wink.move(-eye_close, 0)
        self.left_eye.undraw()
        self.left_eye = eye_wink
        eye_wink.draw(self.window)
        self.smile()
