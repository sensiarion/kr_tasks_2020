import random

h, w = random.randint(4, 12), random.randint(5, 16)

table = []
for i in range(h):
    row = []
    table.append(row)
    for j in range(w):
        row.append(random.randint(1, 30))

max_c = max([max(i) for i in table])
min_c = min([min(i) for i in table])

res = {max_c: [], min_c: []}

for i in range(h):
    for j in range(w):
        if table[i][j] == min_c:
            res[min_c].append((i, j))
        if table[i][j] == max_c:
            res[max_c].append((i, j))


for i in range(h):
    for j in range(w):
        print(table[i][j],end='\t')
    print()

print('---------------------------------------')
print(res)