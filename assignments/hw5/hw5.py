"""
Name: Logan Segal
homework 5.py

Problem: In this homework we practiced working with strings and lists. We worked with reversing
    a string, taking initials from a list, and we even combined this with past topics like with
    loops and arithmatic problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name (first last): ")
    name.split(" ")
    first, last = name.split(" ")
    ", ".join([last, first])
    name_switch = last + ", " + first
    print(name_switch)


def company_name():
    entr_domain = input("enter a domain: ")
    entr_domain.split('.')
    first, mid, last = entr_domain.split('.')
    " ".join([mid, first, last])
    domain = mid
    print(domain)


def initials():
    num_students = eval(input("how many students are in the class? "))
    for i in range(num_students):
        student_name = "what is the name of student " + str(i+1) + "? "
        name = input(student_name)
        name.split()
        first, last = name.split(" ")
        initial = first[0] + last[0]
        print(initial)


def names():
    list_names = input("enter a list of names: ")
    str_to_list = list_names.split(", ")
    for i in str_to_list:
        new_list = i.split(" ")
        first = new_list[0]
        last = new_list[1]
        f_initial = first[0]
        l_initial = last[0]
        initial = f_initial + l_initial
        print(initial, end=" ")


def thirds():
    num_sentences = eval(input("enter the number of sentences: "))
    my_list = []
    for i in range(num_sentences):
        sen = "enter sentence " + str(i+1) + ": "
        sentence = input(sen)
        my_list.append(sentence)
    for j in range(len(my_list)):
        skip = my_list[j][0::3]
        print(skip)


def word_average():
    sentence = input("enter a sentence: ")
    words = sentence.split()
    acc = 0
    total = 0
    for i in words:
        acc = acc + len(i)
        total = total + 1
    average = acc / total
    print(average)


def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin:")
    sentence = sentence.split()
    leftovers = " "
    new_str = " "
    for i in sentence:
        letter = i[0]
        leftover = leftovers + i[1::]
        new_str = new_str + (leftover.lower() + letter.lower() + "ay")
        conversion = new_str.lstrip()
    print(conversion)


if __name__ == '__main__':
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
