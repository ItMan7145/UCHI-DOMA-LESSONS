class Person:

    def __init__(self, name, *args):
        self.name = name
        self.a1 = args[0]
        self.a2 = args[1]

    def say_hi(self):
        print('Hello, my name is ' + self.name)

    def get_data(self):
        print(f'Data: + {self.name} + {self.a1} + {self.a2}')


person1 = Person("Alex", 1, 2)
person1.get_data()
person1.say_hi()
