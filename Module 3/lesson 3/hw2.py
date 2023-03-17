f = open('lines.txt', 'r', encoding='utf8')
a = 0

lines = f.readlines()
for line in lines:
    words = line.split()
    for i in words:
        if isinstance(i, str):
            if i.isalpha():
                if i == i[::-1]:
                    a += 1

print(a)
