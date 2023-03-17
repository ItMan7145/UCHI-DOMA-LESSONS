with open('output.txt', 'r', encoding='utf-8') as file:
    text = file.read()
a = 0
b = ''
for i in text.split():
    if len(i) > a:
        b = i
        a = len(b)

print(b)
