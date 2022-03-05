"""
Name: Logan Segal
homework 7.py

Problem: In this homework we practiced reading and writing files in code. In this
    homework we were given a file, then we opened the file, altered it, then outputted
    it. We combined this with knowledge and problems we have used on previous homeworks.
    We also practiced working with conditionals more.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    i = 0
    for line in in_file:
        words = line.split()
        for word in words:
            i = i + 1
            print(str(i) + " " + word, file=out_file)
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        word = line.split(" ")
        pay = float(word[2])
        bonus = 1.65
        pay_sum = pay + bonus
        hour = float(word[3])
        total_pay = hour * pay_sum
        print(("{}{}{}{}{:.2f}".format(word[0], " ", word[1], " ", total_pay)), file=out_file)
    in_file.close()
    out_file.close()
    print(out_file)


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    check_num = []
    for i in range(10, 0, -1):
        check_num = check_num + [i]
    total = 0
    for i in range(len(isbn)):
        part = int(isbn[i]) * check_num[i]
        total = total + part
    return total


def send_message(file_name, friend_name):
    in_file = open(file_name, 'r')
    out_file= friend_name + ".txt"
    friend_file = open(out_file, 'w')
    file = in_file.read()
    file = file.strip()
    print(file, file=friend_file)


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, 'r')
    out_file = friend_name + ".txt"
    friend_file = open(out_file, 'w')
    og_file = in_file.read()
    safe = encode(og_file, key)
    ord_line = ord("\n") + key
    chr_line = chr(ord_line)
    safe = safe.replace(chr_line, "\n")
    print(safe.rstrip(), file=friend_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file = open(file_name, 'r')
    out_file = friend_name + ".txt"
    friend_file = open(out_file, 'w')
    pad_file = open(pad_file_name, 'r')
    read_in = in_file.read()
    read_pad = pad_file.read()
    uncrackable = encode_better(read_in, read_pad)
    print(uncrackable, file=friend_file)


if __name__ == '__main__':
    pass
