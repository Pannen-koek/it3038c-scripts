import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=2c981c20ee43c401b7c8a7555bad1382' % zip)
data=r.json()
print(data['weather'][0]['description'])