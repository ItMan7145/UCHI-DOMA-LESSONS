SPECIAL = '!@#$%^&*()<>?,.'


class Person:
    def __init__(self, name, password):
        self.name = name
        self.__password = self.check_password(password)

    def check_password(self, password):
        if len(password) < 8:
            raise StupidPasswordError
        elif not set(SPECIAL) & set(password):
            raise StupidPasswordError
        else:
            return password


class StupidPasswordError(Exception):
    def __init__(self):
        print("Расширяй свой запас лексикона!")
        print("Читай больше книг!")


valeriy = Person('Valeriy', 'qwerty!23')
