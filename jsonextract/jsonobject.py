import json
import sys

filename = sys.argv[1]
print(filename)
with open(filename) as json_data:
    d = json.load(json_data)
    print(d)

