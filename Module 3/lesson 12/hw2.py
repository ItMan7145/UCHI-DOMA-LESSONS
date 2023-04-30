import csv

with open('ratings.csv', 'r') as file:
    data = csv.DictReader(file)
    print(data)

    imdb = []
    for i in data:
        # print(i['IMDb Rating'])
        if i['IMDb Rating'] == '9.5':
            imdb.append(i['IMDb Rating'])
    print(len(imdb))
