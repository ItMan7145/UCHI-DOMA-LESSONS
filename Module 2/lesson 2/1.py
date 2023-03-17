import math


class Circle:
    a = 0
    b = 0

    def __init__(self, x=0, y=0, r=0):
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


d1 = Circle()
print(d1.a, d1.b)

Circle.a = 1
Circle.b = 5
Circle.c = 3

d1.z = 10

print(d1.__dict__)
print(Circle.__name__)
print(d1.a, d1.b, d1.c)
delattr(Circle, Circle.a)

# x, y, r = map(int, input('x, y, r: \n').split())
# c1 = Circle(x, y, r)
#
# while 1:
#     who = int(input('?: \n'))
#
#     match who:
#         case 1:
#             print(c1.get_area())
#         case 2:
#             print(c1.get_circle())
#         case 3:
#             k = int(input('k: \n '))
#             c1.set_radius(k)
#             print(c1.r)
#         case 4:
#             x, y, r = map(int, input('x, y, r: \n').split())
#             c2 = Circle(x, y, r)
#             print(c1.is_intersect(c2))
