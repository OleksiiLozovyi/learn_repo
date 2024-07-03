from random import random, randint, choices, sample

def get_numbers_ticket(min=5, max=49, quantity=6):
    try:
        numbers = range(min,max)
        chosen_item = sorted(sample(numbers, k=quantity))
        return chosen_item
    except:
        chosen_item = []
        print ('Min have to be < max')
        return chosen_item
get_numbers_ticket()