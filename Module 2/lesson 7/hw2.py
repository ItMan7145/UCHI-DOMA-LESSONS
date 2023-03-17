class Student:
    def __init__(self, name):
        self.name = name

    def get_action(self):
        return f"Ученик {self.name} учится"

    def __repr__(self):
        return f"Student({self.name})"


class Teacher:
    def __init__(self, name):
        self.name = name

    def get_action(self):
        return f"Учитель {self.name} учит"

    def __repr__(self):
        return f"Teacher({self.name})"


n = int(input())
persons = []

for i in range(n):
    line = input().split(': ')
    if line[0] == 'Student':
        obj = Student(line[1])
    else:
        obj = Teacher(line[1])
    persons.append(obj)

# answer = "[", persons, "]"
# print(answer)
print(persons)

for person in persons:
    print(person.get_action())


# class Person:
#     def init(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}({self.name})'
#
#
# class Student(Person):
#     def get_action(self):
#         return f'Ученик {self.name} учится'
#
#
# class Teacher(Person):
#     def get_action(self):
#         return f'Учитель {self.name} учит'
#
#
# n = int(input())
# persons = []
# for i in range(n):
#     line = input().split(': ')
#     if line[0] == 'Student':
#         obj = Student(line[1])
#     else:
#         obj = Teacher(line[1])
#     persons.append(obj)
# print(persons)
# for person in persons:
#     print(person.get_action())
