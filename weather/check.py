import requests

r = requests.get('https://www.metaweather.com/api/location/2455920')
print(r.text)
d = r.json()
print(d)