import random


def get_random_from_list(list):
    if len(list) == 0:
        return
    return list[random.randint(0, len(list) - 1)]