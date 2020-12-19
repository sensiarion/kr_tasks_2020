import random

height = random.randint(4, 12)
width = random.randint(5, 16)

numbers = sorted(list(range(100, width * height + 102)), key=lambda x: random.random())

table = []
base_table = []
for i in range(height):
    row = []
    for j in range(width):
        row.append(str(numbers.pop()) if random.randint(0, 1) else '')
    table.append(row)
    base_table.append(row.copy())

corrupt = '1215sdgdhu7ue;owfk;2324\/'

rows = []
for i in range(height):
    for j in range(width):
        rnd = random.randint(0, 2)
        if rnd:
            if rnd == 1:
                table[i][j] = f'{random.choice(corrupt)}{table[i][j]}'
            else:
                table[i][j] = f'{table[i][j]}{random.choice(corrupt)}'

    row = ')&'.join(table[i])

    factor = random.random()
    if factor < 0.2:
        rows.append(row)

    rows.append(row)

result = '#!^'.join(rows)

choosed_line = random.randint(0, height-1)

for i in range(height):
    for j in range(width):
        print(base_table[i][j], end='\t')
    print()
print('---------------------------------------------')

print(choosed_line)
print(result)
print('---------------------------------------------')
print('\t'.join(base_table[choosed_line]))
