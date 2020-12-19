import random

count = random.randint(10, 20)
lucky_count = random.randint(2, count // 2)

start_from = count % lucky_count

print(count, lucky_count, sep='\n')
print('---------------------------------------')
numbers = range(count)
lucky_numbers = set(range(start_from, count, count // lucky_count))
print(*[i if i not in lucky_numbers else f'\*{i}\*' for i in numbers])
