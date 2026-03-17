#! python3

import json

# some JSON:
xText =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
xData = json.loads(xText)

yData = {
    "name": "Sally",
    "age" : 25,
    "city": "Washington, DC"
}

yText = json.dumps(yData)

# the result is a Python dictionary:
print(xData["name"])

print(yData["name"])