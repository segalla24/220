"""
Name: Logan Segal
Lab 6.py

Problem: In this lab we are working with encoding and decoding strings.
    We combined this with our previous knowledge of using graphics and
    different operators. In the end, we were able to type in a sentence
    and a keyword, and the code we created helped encode the message using
    the keyword to create a new message.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Text, Point, Entry, Rectangle


def vigenere():
    win = GraphWin("vigenere", 600, 400)

    message_text = Text(Point(175, 100), "message to code:")
    message_entry = Entry(Point(355, 100), 30)
    message_text.setSize(16)
    message_text.draw(win)
    message_entry.draw(win)

    keyword_text = Text(Point(185, 150), "enter keyword:")
    keyword_entry = Entry(Point(355, 150), 30)
    keyword_text.setSize(16)
    keyword_text.draw(win)
    keyword_entry.draw(win)

    button = Rectangle(Point(230, 200), Point(375, 250))
    button_center = button.getCenter()
    button_text = Text(button_center, "encode")
    button.draw(win)
    button_text.setSize(14)
    button_text.draw(win)
    win.getMouse()

    message_gt = message_entry.getText()
    message_together = message_gt.replace(" ", "")
    message_upper = message_together.upper()

    keyword_gt = keyword_entry.getText()
    keyword_together = keyword_gt.replace(" ", "")
    keyword_upper = keyword_together.upper()

    my_string = ""

    for i in range(len(message_upper)):
        msg_num = ord(message_upper[i]) - 65
        key_num = ord(keyword_upper[i % len(keyword_upper)]) - 65
        total = msg_num + key_num
        mod = total % 26
        convert = mod + 65
        revert = chr(convert)
        my_string = my_string + revert

    button.undraw()
    button_text.undraw()
    result_message = Text(button_center, "resulting message")
    result_message.setSize(16)
    result_message.draw(win)
    actual_message = Text(Point(300, 250), my_string)
    actual_message.setSize(14)
    actual_message.draw(win)

    f_struct = Text(Point(300, 385), "click anywhere to close window")
    f_struct.setSize(14)
    f_struct.draw(win)
    win.getMouse()
    win.close()


vigenere()