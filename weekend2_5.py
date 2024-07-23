# def sorted_numbers(list_of_numbers, x):
#     def abs_x(element):
#         return abs(element-x)
#     return sorted(list_of_numbers, key=abs_x)[0]
#
# x=10
# numbers = [5, 9, 12, 5, 1, -9]
# print(sorted_numbers(numbers,x))




def sorted_numbers(list_of_numbers, x):
    return sorted(list_of_numbers, key=lambda el: abs(el-x))[0]

x=10
numbers = [5, 9, 12, 5, 1, -9]
print(sorted_numbers(numbers,x))