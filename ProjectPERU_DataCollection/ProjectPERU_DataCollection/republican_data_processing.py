import io
import re

lines = []

with io.open('labeled_republican_data.txt', 'r', encoding='ascii', errors='ignore') as infile:
    for line in infile:
        lines.append(line.split(','))

count = 0
for line in lines:
    if len(line[1].split(' ')) <= 2 and not "honk" in line[1].lower() and not "imigra" in line[1].lower() and not "womp" in line[1].lower():
        print(line)
        line[0] = '1'
        count += 1

with open('labeled_republican_data.txt', 'w') as outfile:
    for line in lines:
        outfile.write(line[0] + "," + line[1])

print("Lines changed: " + str(count))