line = int(input())
data = input()
rows = [i.split(')&') for i in data.split('#!^')]

for i, row in enumerate(rows):
    for j, element in enumerate(row):
        if element.isdigit():
            continue
        elif element == '':
            continue
        else:
            res = ''
            for k in element:
                if k.isdigit():
                    res += k

            row[j] = res

to_remove = set()

for i in range(len(rows) - 1):
    if rows[i] == rows[i + 1]:
        to_remove.add(i)

temp = []
for i, row in enumerate(rows):
    if i not in to_remove:
        temp.append(row)

rows = temp

print(*rows[line], sep='\t')
