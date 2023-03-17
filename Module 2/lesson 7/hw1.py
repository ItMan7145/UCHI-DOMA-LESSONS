class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        if self.__class__ == Point2D:
            return (self.x ** 2 + self.y ** 2) ** 0.5
        elif self.__class__ == Point3D:
            return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def get_info(self):
        if self.__class__ == Point2D:
            return f'Точка с координатами ({self.x}, {self.y})'
        elif self.__class__ == Point3D:
            return f'Точка с координатами ({self.x}, {self.y}, {self.z})'


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


how_class = input()
x, y, z = map(int, input().split())

if how_class == 'Point2D':
    p1 = Point2D(x, y)
elif how_class == 'Point3D':
    p1 = Point3D(x, y, z)

print(p1.get_distance())
print(p1.get_info())
