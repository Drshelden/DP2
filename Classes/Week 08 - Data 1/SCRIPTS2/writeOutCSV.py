#! python3
import csv
import random

# Generate 10 row lists
n = 11
data = []
for i in range(1, n):
    item = [
        f'name{i:02}',
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    ]
    data.append(item)

with open('C:\\_LOCAL\\writeOutCSV.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'r', 'g', 'b'])
    for item in data:
        writer.writerow(item)

# Read rows back into lists (skip header)
rows = []
with open('C:\\_LOCAL\\writeOutCSV.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        rows.append(row)

print(rows)