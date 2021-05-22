
import requests
import pprint

API_KEY = '7721b9bbcdd316d68ac434ba266b44dd'
city = 'Kiev'
days = 3

url_now = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
url_5 = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
response = requests.get(url_now)
response = response.json()
response5 = requests.get(url_5)
response5 = response.json()
ch = 0


def now(response):
    for key, value in response.items():
        if key == 'main':
            pprint.pprint(key, value)
        if key == 'weather':
            pprint.pprint(key, value)
        if key == 'wind':
            pprint.pprint(key, value)


def five_days(response5):
    for key, value in response5.items():
        if key == 'main':
            pprint.pprint(key, value)
        if key == 'weather':
            pprint.pprint(key, value)
        if key == 'wind':
            pprint.pprint(key, value)
        ch += 1
        if ch >= 3:
            break






