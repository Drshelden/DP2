#! python3
import random

# Generate 10 dictionaries
n = 11
data = []
for i in range(1, n):
    item = {
        'name': f'name{i:02}',
        'r': random.randint(0, 255),
        'g': random.randint(0, 255),
        'b': random.randint(0, 255)
    }
    data.append(item)


with open('C:\\_LOCAL\\fileout.csv', mode='w') as file:
    file.write('name,r,g,b\n')  # Write header
    for item in data:
        file.write(f"{item['name']},{item['r']},{item['g']},{item['b']}\n")