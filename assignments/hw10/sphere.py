"""
Name: Logan Segal
Homework 10.py

Problem: In this homework we are working with creating our own classes and functions.
    We created everything from a blank coding page, and coded everything ourselves
    from start to finish. This homework utilizes everything we have learned so far, with
    the new topics we have learned about creating our own classes.


Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from math import pi


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.vol = 0

    def get_radius(self):
        return self.radius

    def surface_area(self):
        self.area = 4 * pi * (self.radius ** 2)
        return self.area

    def volume(self):
        self.vol = (4 / 3) * pi * (self.radius ** 3)
        return self.vol
