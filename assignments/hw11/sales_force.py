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
from sales_person import SalesPerson


class SalesForce:
    """
    This is a class to collect data of different sales people
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        for line in infile.readlines():
            split = line.split(",")
            the_id = split[0]
            the_id = int(the_id)
            name = split[1].strip()
            sales = split[2].strip().split(" ")
            employee = SalesPerson(the_id, name)
            for i in range(len(sales)):
                employee.enter_sale(float(sales[i]))
            self.sales_people += [employee]
        infile.close()

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            my_list = []
            employee_id = person.get_id()
            employee_name = person.get_name()
            employee_total = person.total_sales()
            employee_quota = person.met_quota(quota)
            my_list.append(employee_id)
            my_list.append(employee_name)
            my_list.append(employee_total)
            my_list.append(employee_quota)
            report.append(my_list)
        return report

    def top_seller(self):
        top_list = []
        top_sales = []
        for i in self.sales_people:
            sales = i.get_sales()
            sales.sort()
            best_sale = sales[-1]
            top_sales.append(best_sale)
            top_sales.sort()
        if top_sales[-1] != top_sales[-2]:
            for j in self.sales_people:
                if top_sales[-1] in j.get_sales():
                    top_list.append(j)
                    return top_list
        elif top_sales[-1] == top_sales[-2]:
            for k in self.sales_people:
                if top_sales[-1] in k.get_sales():
                    top_list.append(k)
                if top_sales[-2] in k.get_sales():
                    top_list.append(k)
                    return top_list

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if employee_id == i.get_id():
                return i

    def get_sale_frequencies(self):
        my_list = []
        for i in self.sales_people:
            sales = i.get_sales()
            my_list.append(sales)
        frequency = {}
        for j in my_list:
            for k in j:
                if k in frequency:
                    frequency[k] += 1
                else:
                    frequency[k] = 1
        return frequency
