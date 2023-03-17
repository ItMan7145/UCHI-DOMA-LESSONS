spisok = [1, 2, 3, 4, 5]
print(spisok)

spisok.append("a")
spisok.insert(3, 432)
print(spisok)

spisok2 = [1, 2, 3]
spisok.append(spisok2)
print(spisok)

korteg = (1, 2, 3, 4, 5)
spisok.append(korteg)
print(spisok)

print(spisok[1])

spisok.remove(3)
print(spisok)

print(spisok.count(2))
