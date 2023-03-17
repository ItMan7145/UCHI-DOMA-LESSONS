from sys import stdin

total = []
for line in stdin:
    total.append(line)

print(total)
with open('output.txt', 'w', encoding='utf-8') as file:
    for line in total:
        file.write(line)
