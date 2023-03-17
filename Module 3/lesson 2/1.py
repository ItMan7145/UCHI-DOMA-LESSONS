# def f():
#     x = 'enclosing'
#     def g():
#         print(x)
#     g()
# f()
#


# def mul(x):
#     def func(y):
#         return x * y
#
#     return func
#
#
# mul5 = mul(5)
# print(mul5(2))
# print(mul5(3))
# print(mul5(4))


# def decor(func):
#     def wrapper(*args, **kwargs):
#         print('Start')
#         func()
#         print('Stop')
#     return wrapper
#
#
# @decor
# def test():
#     print('test')
#
#
# test()


# a = [1, 2, 3]
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))


# def generator():
#     i = 1
#     # yield i
#     # i += 1
#     # yield i
#     # i += 1
#     # yield i
#     while 1:
#         yield i
#         i += 1
#
#
# g = generator();print(next(g));print(next(g));print(next(g))
#


def num_gen(x, y):
    while 1:
        for i in range(x, y + 1):
            yield i


a = num_gen(0, 10)
# for i in range(20):
print(next(a))
print(next(a))
print(a.__next__())
print(list(a))
