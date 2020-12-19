from typing import Tuple
import random


def generate_user(id: int) -> Tuple[int, str, str, int, str]:
    """
    Создаёт пользователя с указанным идентификатором
    :param id: идентификатор пользователя
    :return: информация о пользователе (идентификатор,имя,фамилия,возраст, школа)
    """

    male_names = ('Вася', 'Петя', 'Миша', 'Коля', 'Гоша', 'Максим')
    female_names = ('Оля', 'Катя', 'Вика', 'Настя', 'Даша', 'Ксюша')
    surnames = ('Петров', 'Иванов', 'Чугунов', 'Столяров', 'Максимов', 'Торов', 'Башмаков')
    schools = ('Первая школа', 'Вторая школа', 'Третья школа', 'Гимназия', 'Пятая школа', 'Четвёртая школа')

    if random.random() > 0.5:
        name = random.choice(male_names)
        surname = random.choice(surnames)
    else:
        name = random.choice(female_names)
        surname = random.choice(surnames) + 'а'

    return id, name, surname, random.randint(8, 14), random.choice(schools)


