import json
from pprint import pprint
from random import randint
#json_data=open('dump2.json')
#json_data=open('datadump.json')
json_data=open('rawdump2.json')
data = json.load(json_data)
# pprint(data)
for d in data:
    year = d['year']
    age = 2012 - int(year)
    if age < 21 or age > 57:
        age = 21 + randint(0,15)
    d['year'] = unicode(2012 - age)
pprint(data)
json_data.close()

# With data, you can now also find values in like so:
# data["maps"][0]["id"]
# data["masks"]["id"]
# data["om_points"]
