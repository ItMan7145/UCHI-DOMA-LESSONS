from math import pi

a = int(input())
b = int(input())


def square(a, b):
    print(a * b)


def triangle(a, b):
    print(a * b * 0.5)


def circle(a):
    print(pi * a ** 2)


square(a, b)
triangle(a, b)
circle(a)
