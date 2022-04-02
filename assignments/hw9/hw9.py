"""
Name: Logan Segal
Homework 9.py

Problem: In this homework we are putting all of our knowledge to the test by creating
    a game of Hangman. After creating all our functions, we created two different versions,
    one that is run through the terminal and another that is created through graphics.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin,Text, Point, Entry, Line, Circle


def get_words(file_name):
    my_file = open(file_name, "r")
    my_list = []
    lines = my_file.readlines()
    for line in lines:
        my_list.append(line)
    return my_list


def get_random_word(words):
    random_word = randint(0, len(words)-1)
    got_word = words[random_word]
    secret_word = got_word.rstrip()
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    blanks = [] * len(secret_word)
    for i in range(len(secret_word)):
        blanks.append('_')
    my_list = []
    my_list[:] = secret_word
    for word in range(len(secret_word)):
        for j in range(len(guesses)):
            if guesses[j] == my_list[word]:
                blanks[word] = guesses[j] + ''
    return ' '.join(blanks)


def won(guessed):
    for guess in guessed:
        if guess == "_":
            return False
    return True


def play_graphics(secret_word):
    win = GraphWin("Hangman", 700, 700)

    top = Line(Point(200, 100), Point(370, 100))
    top.draw(win)
    hang_line = Line(Point(200, 100), Point(200, 165))
    hang_line.draw(win)
    vertical = Line(Point(370, 100), Point(370, 550))
    vertical.draw(win)
    bottom = Line(Point(175, 550), Point(450, 550))
    bottom.draw(win)

    head = Circle(Point(200,210), 45)
    body = Line(Point(200,255), Point(200,425))
    leg1 = Line(Point(150,500),Point(200,425))
    leg2 = Line(Point(250,500), Point(200,425))
    arm1 = Line(Point(150,300), Point(200,350))
    arm2 = Line(Point(250,300), Point(200,350))

    letter_text = Text(Point(275, 625), "guess a letter:")
    letter_entry = Entry(Point(360, 625), 5)
    letter_text.setSize(16)
    letter_text.draw(win)
    letter_entry.draw(win)

    my_list = []
    guess_amount = 6
    correct_guess = make_hidden_secret(secret_word, my_list)
    while guess_amount >= 0 and not correct_guess == secret_word:
        win.getKey()
        get_entry = letter_text.getText()
        letter_text.setText("")
        my_list.append(get_entry)
        if letter_in_secret_word(get_entry, secret_word):
            correct_guess = make_hidden_secret(secret_word, my_list)

        else:
            guess_amount -= 1
            if guess_amount == 5:
                head.draw(win)
            elif guess_amount == 4:
                body.draw(win)
            elif guess_amount == 3:
                leg1.draw(win)
            elif guess_amount == 2:
                leg2.draw(win)
            elif guess_amount == 1:
                arm1.draw(win)
            elif guess_amount == 0:
                arm2.draw(win)

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    my_list = []
    guess_amount = 6
    correct_guess = make_hidden_secret(secret_word, my_list)
    while guess_amount >= 0 and not correct_guess == secret_word:
        print("already guessed:", my_list)
        print("guesses remaining:", guess_amount)
        print(correct_guess)
        letter = input("guess a letter: ")
        my_list.append(letter)
        if letter_in_secret_word(letter, secret_word):
            correct_guess = make_hidden_secret(secret_word, my_list)
        else:
            guess_amount -= 1
        if correct_guess.split(" ") == list(secret_word):
            print("winner!\n" + correct_guess)
            break
        elif guess_amount == 0:
            print("sorry, you did not guess the word.")
            print("the secret word was " + secret_word)
        else:
            print()


# complete = "_" * len(secret_word)
    # guessed = False
    # guessed_letters = []
    # guessed_words = []
    # tries = 6
    # while not guessed and tries > 0:
    #     guess =


if __name__ == '__main__':
    # play_command_line("time")
    play_graphics("time")
