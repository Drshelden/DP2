#! python3
#r: requests
import json

import requests

# Define the API endpoint for the National Weather Service
url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    # data = response.json()
    # print(data)
    myText = response.text
    myJson = myText.replace("'", '"')
    myData = json.loads(myJson)
    myGeometry = myData.get('geometry').get('coordinates').getItem(0)

    print(myGeometry)
else:
    print(f"Failed to retrieve data: {response.status_code}")