n = int(input())
lucky_n = int(input())

numbers = range(0, n)
lucky_numbers = set(range(n % lucky_n, n, n // lucky_n))

print(*[i if i not in lucky_numbers else f'*{i}*' for i in numbers])
