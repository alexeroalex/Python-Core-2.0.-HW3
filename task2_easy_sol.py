import random


def get_numbers_ticket(min_num, max_num, quantity):
    choice_interval = list(range(min_num, max_num))
    res_list = random.sample(choice_interval, quantity)
    res_list.sort()
    return res_list


print(get_numbers_ticket(1, 10, 4))
