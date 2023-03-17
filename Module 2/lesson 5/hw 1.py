# class Sequence:
#     def __init__(self, spisok):
#         self.spisok = spisok
#
#     def __add__(self, other):
#         for elem in other.num_list:
#             if elem not in self.spisok:
#                 self.spisok.append(elem)
#         return self.spisok
#
#     def __str__(self):
#         return f"Последовательность {self.spisok}"


class Sequence:
    def __init__(self, nums_list):
        self.nums_list = nums_list

    def __add__(self, other):
        for el in other.nums_list:
            if el not in self.nums_list:
                self.nums_list.append(el)
        return self.nums_list

    def __str__(self):
        return f'Последовательность {self.nums_list}'


s1 = ['1', '1', '2', '4']
s2 = ['3', '4', '5', '1', '6']

a = Sequence(s1)
b = Sequence(s2)

print(a + b)
