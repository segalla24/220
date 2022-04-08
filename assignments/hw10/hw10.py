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
from graphics import GraphWin, Point
from face import Face


def fibonacci(num):
    acc1 = 1
    acc2 = 1
    fibonacci_sequence = []
    count = 0
    while count < num and num > 1:
        fibonacci_sequence.append(acc1)
        result = acc1 + acc2
        acc1 = acc2
        acc2 = result
        count += 1
    return fibonacci_sequence[num - 1]


def double_investment(principle, rate):
    year = 0
    total = principle
    while total <= 2 * principle:
        total = total + total * rate + 1
        year += 1
    return year


def syracuse(num):
    my_list = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        my_list.append(num)
    return my_list


def goldbach(num):
    primes = []
    value = 1
    while value <= num:
        count = 0
        i = 2
        while i <= value // 2:
            if value % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and value != 1:
            primes.append(value)
        value = value + 1

    if num % 2 != 0:
        return None

    index_a = 0
    index_b = 0
    prime_a = primes[index_a]
    prime_b = primes[index_b]

    while prime_a + prime_b != num:
        if prime_b == primes[-1]:
            index_a = index_a + 1
            index_b = index_a + 1
            prime_a = primes[index_a]
            prime_b = primes[index_b]
        else:
            index_b = index_b + 1
            prime_b = primes[index_b]
    return [prime_a, prime_b]


def main():
    win = GraphWin("Face", 700, 700)
    my_face = Face(win, Point(350, 350), 300)
    #my_face.wink()
    my_face.smile()
    #my_face.shock()
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
