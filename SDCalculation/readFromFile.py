import json
from pprint import pprint

with open('data/data.json') as data_file:
    data = json.load(data_file)

print data["zAxis"]
#pprint(data)