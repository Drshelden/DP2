#! python3

import random
import csv

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

print(data)


with open('C:\\_LOCAL\\file.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'r', 'g', 'b'])  # Write header
    for item in data:
        writer.writerow([item['name'], item['r'], item['g'], item['b']])