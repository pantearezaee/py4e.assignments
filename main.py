import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum=0
tree = ET.fromstring(urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1316320.xml").read()).findall('comments/comment')
for count in tree: sum += int(count.find('count').text)
print(sum)
