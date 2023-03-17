class Person:
    def __init__(self, name, age, passport):
        self.__name = name
        self.__age = age
        self.__passport = passport

    def change_age(self):
        self.__age += 1

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, new_passport):
        if len(new_passport) == 10:
            self.__passport = new_passport
        else:
            print('Неверный номер паспорта')

    def get_info(self):
        passport_num = list(self.__passport)

        for i in range(0, 6):
            passport_num[i] = '*'

        passport_num = ''.join(passport_num)

        return f'{self.__name}, возраст: {self.__age}, номер паспорта: {passport_num}'


name = input()
age = int(input())
passport = input()
method = input()

person = Person(name, age, passport)

if method.isdigit():
    person.passport = method
elif method == 'change_age':
    person.change_age()

print(person.get_info())
