class Ground:
    title = 'Ground'
    count = 0

    def __init__(self):
        Ground.count += 1

    def __add__(self, obj):
        if isinstance(obj, Water):
            return "Грязь!"
        elif isinstance(obj, Fire):
            return "Песок!"
        elif isinstance(obj, Air):
            return "Пыль!"
        else:
            return "Алхимический стол сделал бум!"

    def __radd__(self, obj):
        if isinstance(obj, Water):
            return "Грязь!"

    def __str__(self):
        return "Это класс земля"

    def __len__(self):
        print("Количество грязи: ", end='')
        return Ground.count


class Water:
    title = 'Water'


class Fire:
    title = 'Fire'


class Air:
    title = 'Air'


gnd = Ground()
water = Water()

sth = {"земля": Ground(),
       "огонь": Fire(),
       "вода": Water(),
       "воздух": Air()}

elem = input("Введите название элемента: ")

second_element = sth[elem]
print(gnd + second_element)
