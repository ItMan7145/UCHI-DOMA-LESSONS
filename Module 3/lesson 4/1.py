import json

with open('starwars_3.json') as file:
    data = json.load(file)

pers = set()
for i in data['results']:
    for j in i['characters']:
        pers.add(j)


print(pers)
print(len(pers))