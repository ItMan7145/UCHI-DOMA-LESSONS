# from math import gcd

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
#
# if a2 == b2:
#     print(a1 + b1, a2)
# else:
#     cd = int(b1 * b2 / gcd(b1, b2))


a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())

num1 = a1 * b2 + b1 * a2
num2 = a2 * b2

num3, num4 = num1, num2

while num1 != 0:
    if num1 < num2:
        num1, num2 = num2, num1
    num1 %= num2

print(num3 // num2, num4 // num2, sep="\n")
