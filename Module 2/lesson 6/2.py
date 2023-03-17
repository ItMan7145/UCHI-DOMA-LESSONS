# BashAutoTrans PROGRAM

import math


class Auto:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, dist):
        self.x += dist * math.cos(self.direction)
        self.y += dist * math.sin(self.direction)

    def set_direction(self, new_direction):
        self.direction = new_direction


class Bus(Auto):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def enter_passengers(self, new_passengers):
        self.passengers += new_passengers

    def exit_passengers(self, exit_passengers):
        self.passengers -= exit_passengers


def get_direction():
    direction = int(input("""Выберите направление движения:
    1 - север
    2 - запад
    3 - юг
    4 - восток
    
Куда едем?: """))

    match direction:
        case 1:
            return math.radians(90)
        case 2:
            return math.radians(180)
        case 3:
            return math.radians(270)
        case 4:
            return math.radians(0)


bus1 = Bus(0, 0, get_direction())

while 1:
    print("\nОстановка!")

    if bus1.passengers > 0:
        exit_passengers = int(input("Сколько пассажиров вышло?: "))
        bus1.exit_passengers(exit_passengers)

    bus1.enter_passengers(int(input("Сколько вошло пассажиров?: ")))
    bus1.move(int(input("Сколько автобус проехал?: ")))

    print(bus1.money, bus1.x, bus1.y)

    bus1.set_direction(get_direction())
