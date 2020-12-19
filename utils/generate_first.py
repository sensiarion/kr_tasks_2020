import random

from utils.user_generator import generate_user

gen_card_numb = lambda: random.randint(1_000, 9_999)
gen_summ = lambda: random.randint(10, 99) * 100


if __name__ == '__main__':

    correct_card = gen_card_numb()
    correct_count = 0
    enough = gen_summ()
    not_correct = []

    user_info = []

    count = random.randint(4, 12)

    for i in range(count):
        is_correct = bool(random.randint(0, 1))

        user_sum = gen_summ()
        t = generate_user(i)

        send_to = gen_card_numb() if not is_correct else correct_card
        transaction = f'перевод с карты {gen_card_numb()} {t[1]} {t[2]} ' \
                      f'на карту {send_to} в размере {user_sum} рублей'

        user_info.append(transaction)

        if not is_correct:
            not_correct.append(f'{t[1]} {t[2]} необходимо доплатить ещё {enough} рублей')
        elif user_sum < enough:
            not_correct.append(f'{t[1]} {t[2]} необходимо доплатить ещё {enough - user_sum} рублей')
        else:
            correct_count += 1

    print(count, correct_card, enough, sep='\n')
    for inf in user_info:
        print(inf)

    print('------------------------------------')
    print(correct_count)
    for inf in not_correct:
        print(inf)
