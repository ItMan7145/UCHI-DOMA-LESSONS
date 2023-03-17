class OddEvenList(list):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

    def get_even(self):
        r_list = []
        for el in self.obj:
            if el % 2 == 0:
                r_list.append(el)
        return r_list

    def get_odd(self):
        r_list = []
        for el in self.obj:
            if el % 2 != 0:
                r_list.append(el)
        return r_list


input_list = []
n = int(input())
for i in range(0, n):
    ch = int(input())
    input_list.append(ch)

a = OddEvenList(input_list)

print(a.get_even())
print(a.get_odd())
