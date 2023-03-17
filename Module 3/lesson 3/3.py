with open("file.txt") as file:
    text = file.read().split()

for i in text:
    if i[::-1] == i:
        print(i)
