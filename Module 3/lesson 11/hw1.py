import datetime
import json

with open('response (1).json', 'r') as file:
    response = json.load(file)

sunrise = response['sys']['sunrise']
sunset = response['sys']['sunset']

time1 = datetime.datetime.fromtimestamp(sunrise)
time2 = datetime.datetime.fromtimestamp(sunset)

print(time1.strftime('%H:%M'))
# print(time2.strftime('%H:%M'))
