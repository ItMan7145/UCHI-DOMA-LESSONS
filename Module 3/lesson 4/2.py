import csv

with open('starwars.csv') as file:
    data = csv.reader(file)
    # print(data)

    person = ""
    height = 0
    for i in data:
        # print(i[0], i[1])
        if i[1].isdigit() and int(i[1]) > int(height):
            height = int(i[1])
            person = i[0]

print("САМЫЙ ВЫСОКИЙ: ", person, height)

print("""
Цитаты великих:
" int(0) " - Арслан.
""")
