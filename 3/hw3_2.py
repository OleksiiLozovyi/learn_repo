from random import random, randint, choices

def get_numbers_ticket(min=1, max=49, quantity=6):
    numbers = range(min,max)
    chosen_item = sorted(choices(numbers, k=quantity))
    print(chosen_item)
get_numbers_ticket()