import random

"""
    Генерує набір з унікальних цілих чисел для лотереї.

    Параметри:
    min_num (int): Мінімальне число для генерації.
    max_num (int): Максимальне число для генерації.
    quantity (int): Кількість випадкових чисел для генерації.
    
    Повертає:
    list[int]: Список з унікальними числами.
    """


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    # Перевірка правильності лімітів
    if min_num < 1 or max_num > 1000:
        return []

    # quantity не може бути більша за саму довжину інтервалу
    elif quantity > len(range(min_num, max_num + 1)):
        return []

    else:
        # Конвертація у список задля подальшого використання remove()
        choice_interval = list(range(min_num, max_num + 1))
        res_list = []

        # Додавання випадкового елемента і видалення для унікальності
        for i in range(quantity):
            x = random.choice(choice_interval)
            res_list.append(x)
            choice_interval.remove(x)
            res_list.sort()
        return res_list


print('Випадкові числа:', get_numbers_ticket(1, 10, 4))
