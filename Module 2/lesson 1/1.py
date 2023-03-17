import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_circle(self):
        return 2 * math.pi * self.r

    def set_radius(self, k):
        self.r *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


x, y, r = map(int, input('x, y, r: \n').split())
c1 = Circle(x, y, r)

while 1:
    who = int(input('?: \n'))

    match who:
        case 1:
            print(c1.get_area())
        case 2:
            print(c1.get_circle())
        case 3:
            k = int(input('k: \n '))
            c1.set_radius(k)
            print(c1.r)
        case 4:
            x, y, r = map(int, input('x, y, r: \n').split())
            c2 = Circle(x, y, r)
            print(c1.is_intersect(c2))
