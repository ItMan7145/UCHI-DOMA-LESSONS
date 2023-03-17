# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

import math


def fib(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi ** n - psi ** n) / math.sqrt(5))


n = 3 ** 3 ** 3 ** 3 ** 3
print(n)
# print(fib(n))
