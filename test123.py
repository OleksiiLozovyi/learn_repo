import random

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=3)
print(chosen_item)