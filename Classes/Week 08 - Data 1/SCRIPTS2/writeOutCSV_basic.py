#! python3
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

with open('C:\\_LOCAL\\writeOutCSV_basic.csv', mode='w') as file:
    file.write('name,r,g,b\n')
    for item in data:
        row_text = ','.join(str(value) for value in item)
        file.write(row_text + '\n')

# Read rows back into lists (skip header)
rows = []
with open('C:\\_LOCAL\\writeOutCSV_basic.csv', mode='r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        row = line.strip().split(',')
        rows.append(row)

print(rows)

