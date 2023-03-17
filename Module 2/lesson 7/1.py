class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"""
        Имя: {self.name}, Возраст: {self.age}
        Должность: {self.post}, Зарплата: {self.calc_salary()}"""


class Manager(Person):
    post = 'Менеджер'

    def calc_salary(self):
        return 50000


class Agent(Person):
    post = "Агент по недвижимости"

    def calc_salary(self):
        return 10000 + 0.05 * 1000000


class Waiter(Person):
    post = "Официант"

    def calc_salary(self):
        return 67 * 200


m = Manager("Валерий С", 28)
a = Agent("Владимир П", 70)
w = Waiter("Михаил М", 56)

print(m)
print(a)
print(w)
