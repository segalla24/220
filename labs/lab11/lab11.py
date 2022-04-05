"""
Name: Logan Segal
lab 11.py

Problem: This lab is a continuation of last week's lab; however, now we are creating a game.
    We are combining all of our previous information that we have learned so far to complete
    this lab.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from door import Door
from button import Button
from graphics import GraphWin,Rectangle, Point, Text
from random import randint


def thee_door_game():
    win = GraphWin("Three Door Game", 700, 700)
    win.setBackground("dodgerblue3")

    quit = Button(Rectangle(Point(475, 50), Point(625, 150)), "quit")
    quit.color_button("dodgerblue3")
    quit.draw(win)

    win_txt = Text(Point(150,40), "Wins")
    win_txt.setSize(14)
    win_txt.draw(win)
    win_box = Rectangle(Point(100,50), Point(200,150))
    win_box.setFill("dodgerblue3")
    win_box.draw(win)

    loss_txt = Text(Point(250,40), "Losses")
    loss_txt.setSize(14)
    loss_txt.draw(win)
    loss_box = Rectangle(Point(200, 50), Point(300, 150))
    loss_box.setFill("dodgerblue3")
    loss_box.draw(win)

    door1 = Door(Rectangle(Point(275, 250), Point(425, 600)), "Door 2")
    door1.color_door("salmon4")
    door1.draw(win)

    door2 = Door(Rectangle(Point(500, 250), Point(650, 600)), "Door 3")
    door2.color_door("salmon4")
    door2.draw(win)

    door3 = Door(Rectangle(Point(50, 250), Point(200, 600)), "Door 1")
    door3.color_door("salmon4")
    door3.draw(win)

    secret_msg = Text(Point(350,200), "I have a secret door")
    secret_msg.setSize(14)
    secret_msg.draw(win)

    click_msg = Text(Point(350,650), "Click to guess which is the secret door!")
    click_msg.setSize(14)
    click_msg.draw(win)

    win_msg = Text(Point(350,200), "You Win!")
    win_msg.setSize(14)
    loss_msg = Text(Point(350,200), "Sorry, Incorrect!")
    loss_msg.setSize(14)
    play_again_msg = Text(Point(350,650), "click anywhere to play again")
    play_again_msg.setSize(14)

    secret = randint(1,3)
    if secret == 1:
        door1.set_secret(True)
    elif secret == 2:
        door2.set_secret(True)
    elif secret == 3:
        door3.set_secret(True)

    my_wins = []
    my_losses = []
    win_num = Text(Point(150, 100), "")
    win_num.setSize(14)
    win_num.draw(win)
    win_num.setText(len(my_wins))
    loss_num = Text(Point(250, 100), "")
    loss_num.setSize(14)
    loss_num.draw(win)
    loss_num.setText(len(my_losses))

    point = win.getMouse()
    while not quit.is_clicked(point):
        if door1.is_secret() and door1.is_clicked(point):
            door1.color_door("green")
            my_wins.append('w')
            win_num.setText(len(my_wins))
            secret_msg.undraw()
            win_msg.draw(win)
            click_msg.undraw()
            play_again_msg.draw(win)
        elif door2.is_secret() and door2.is_clicked(point):
            door2.color_door("green")
            my_wins.append('w')
            win_num.setText(len(my_wins))
            secret_msg.undraw()
            win_msg.draw(win)
            click_msg.undraw()
            play_again_msg.draw(win)
        elif door3.is_secret() and door3.is_clicked(point):
            door3.color_door("green")
            my_wins.append('w')
            win_num.setText(len(my_wins))
            secret_msg.undraw()
            win_msg.draw(win)
            click_msg.undraw()
            play_again_msg.draw(win)
        else:
            if not door1.is_secret() and door1.is_clicked(point):
                door1.color_door("red")
                if door2.is_secret():
                    door2.color_door("green")
                if door3.is_secret():
                    door3.color_door("green")
                my_losses.append('l')
                loss_num.setText(len(my_losses))
                secret_msg.undraw()
                loss_msg.draw(win)
                click_msg.undraw()
                play_again_msg.draw(win)
            elif not door2.is_secret() and door2.is_clicked(point):
                door2.color_door("red")
                if door1.is_secret():
                    door1.color_door("green")
                if door3.is_secret():
                    door3.color_door("green")
                my_losses.append('l')
                loss_num.setText(len(my_losses))
                secret_msg.undraw()
                loss_msg.draw(win)
                click_msg.undraw()
                play_again_msg.draw(win)
            elif not door3.is_secret() and door3.is_clicked(point):
                door3.color_door("red")
                if door1.is_secret():
                    door1.color_door("green")
                if door2.is_secret():
                    door2.color_door("green")
                my_losses.append('l')
                loss_num.setText(len(my_losses))
                secret_msg.undraw()
                loss_msg.draw(win)
                click_msg.undraw()
                play_again_msg.draw(win)
        point = win.getMouse()
        if quit.is_clicked(point):
            win.close()
        else:
            door1.color_door("salmon4")
            door2.color_door("salmon4")
            door3.color_door("salmon4")
            win_msg.undraw()
            loss_msg.undraw()
            play_again_msg.undraw()
            secret_msg.draw(win)
            click_msg.draw(win)
            point = win.getMouse()

    win.close()
thee_door_game()