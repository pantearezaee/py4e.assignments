import json
import urllib.request
import urllib.parse
import urllib.error
counts = list()

address = input("Enter location: ")
print('Retrieving', address)

data = json.loads(urllib.request.urlopen(address).read().decode())
for item in data["comments"]: counts.append(item['count'])
print(sum(counts))

