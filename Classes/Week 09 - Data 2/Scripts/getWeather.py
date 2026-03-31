#! python3
#r: requests
import json
import rhinoscriptsyntax as rs

import requests

# Define the API endpoint for the National Weather Service
url = 'http://localhost:5000/api/components?models=HelloWall-01&componentTypes=IfcShapeRepresentationComponent'
#url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    # data = response.json()
    # print(data)
    myText = response.text
    myJson = myText.replace("'", '"')
    print(myJson)
else:
    print(f"Failed to retrieve data: {response.status_code}")

myData = json.loads(myJson)
print(myData)