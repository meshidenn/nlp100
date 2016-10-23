import json
import re

f = open('jawiki-country.json')
g = open('jawiki-england.txt','w')

for line in f:
    data = json.loads(line)
    if re.search('イギリス',data['title']):
        g.write(data["text"])
        break

f.close
g.close
