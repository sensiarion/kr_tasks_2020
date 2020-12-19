import sys

raw = sys.stdin.read().split('\n')

table = []

for row in raw:
    table.append([int(i) for i in row.split()])

max_value = max([max(row) for row in table])
min_value = min([min(row) for row in table])

result = {max_value:[],min_value:[]}

for i,row in enumerate(table):
    for j, element in enumerate(row):
        if (element == max_value) or (element == min_value):
            result[element].append((i,j))

print(result)