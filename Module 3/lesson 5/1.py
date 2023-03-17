import argparse

a = {"add": lambda x, y: x + y,
     "mul": lambda x, y: x - y,
     "sub": lambda x, y: x * y,
     "div": lambda x, y: x / y}

parser = argparse.ArgumentParser()

parser.add_argument('a', type=int)
parser.add_argument('b', type=int)
parser.add_argument('-o', choices=['add', 'sub', 'mul', 'div'], default='add')

args = parser.parse_args()

try:
    print(a[args.o]), (args.a, args.b)
except ZeroDivisionError:
    print('Ошибка')
