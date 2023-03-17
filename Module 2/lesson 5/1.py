class MyDict(dict):
    def get(self, key, default_val=0):
        return super().get(key, default_val)

    def __getitem__(self, item, default_val=0):
        if hasattr(MyDict, str(item)) is False:
            return 0

    def __add__(self, obj):
        if isinstance(obj, list):
            for i in obj:
                if i not in self.keys():
                    self[i] = 0
        return self

    def __sub__(self, obj):
        if isinstance(obj, list):
            for i in obj:
                if i in self.keys():
                    self.pop(i)
        return self

    def __call__(self):
        average = self.values()
        average = sum(average) / len(average)
        return average


a = MyDict({1: 1, 2: 2})
print(a.get(3))

students = [2, 3, 4, 5]
print(a + students)
print(a - 1)

print(a())
