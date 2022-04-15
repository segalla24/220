"""
Name: Logan Segal
Homework 11.py

Problem: In this homework we are working with creating our own classes. In these classes
    we practice initializing variables and creating methods that can be used in our main
    code. We also practiced importing files and working with lists, along with all the
    previous knowledge we have learned in python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    This class represents the information of different sales people
    """
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc = acc + sale
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        component_1 = self.total_sales() == quota
        component_2 = self.total_sales() > quota
        if component_1 or component_2:
            return True
        else:
            return False

    def compare_to(self, other):
        total = self.total_sales()
        other_sales = other.total_sales()
        if other_sales > total:
            return -1
        if other_sales < total:
            return 1
        return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())

