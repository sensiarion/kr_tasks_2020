n = int(input())
card_number = input()
enough = int(input())

people = []

success = 0

for _ in range(n):
    info = input()
    elems = info.split()
    name = elems[4] + ' ' + elems[5]
    sent_to = elems[8]
    summ = int(elems[11])

    if sent_to != card_number:
        people.append(f'{name} необходимо доплатить ещё {enough} рублей')
        continue
    if summ < enough:
        people.append(f'{name} необходимо доплатить ещё {enough - summ} рублей')
    else:
        success += 1

print(success)
print('\n'.join(people))
