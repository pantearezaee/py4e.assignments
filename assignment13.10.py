import urllib.error, urllib.request, urllib.parse
import json

target = 'http://py4e-data.dr-chuck.net/json?'
url = target + urllib.parse.urlencode({'address': input('Enter location: ') , 'key' : 42})

print('Retriving:', url)
data = urllib.request.urlopen(url).read()
print('Retrived:', len(data), 'characters')
js = json.loads(data)
print('Place id:', js['results'][0]['place_id'])