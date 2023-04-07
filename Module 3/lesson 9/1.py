import requests

response = requests.get('https://google.com/')
response.encoding = 'utf-8'

print(response.text)
print(response.content)
