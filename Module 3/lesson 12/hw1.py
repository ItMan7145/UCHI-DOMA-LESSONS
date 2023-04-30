import json

with open('starwars.json', 'r') as file:
    data = json.load(file)

num = 0
for key in data['results']:
    print(key['director'])
    if key['director'] == 'George Lucas':
        num += 1

print(num)
