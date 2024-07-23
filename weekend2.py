# 1. Дан рядок.
# Розріжте його навпіл і переставте ці половинки містами.
# Якщо довжина непарна, то перша частина буде більшою.

old_str = 'hello world happy, new year and long time ego.'
first_part = old_str[ :len(old_str)//2]
second_part = old_str[len(old_str)//2: ]
# if len(old_str) % 2 == 1:
#     mid_index = len(old_str)//2 + 1
# else:
#     mid_index = len(old_str) // 2

mid_index = len(old_str) // 2 + len(old_str) % 2

first_part = old_str[ :mid_index]
second_part = old_str[mid_index: ]
print(second_part+first_part)
