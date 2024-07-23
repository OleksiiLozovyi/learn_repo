# Заданий непустий список цілих чисел. В цій задачі тобі потрібно повернути список або інший ітеративний об('єкт (кортеж, генератор, '
# 'ітератор), який складається '
# 'тільки з неунікальних елементів '
# 'початкового списку. Для цього необхідно видалити всі унікальні елементи (тобто ті, які наявні в списку тільки один раз). '
# 'Наприклад: в [1, 2, 3, 1, 3], де 1, 3 - неунікальні елементи і результатом буде [1, 3, 1, 3].)



def checkio(numbers):
    list_of_numbers = []
    for elem in numbers:
        number = numbers.count(elem)
        if number > 1:
            list_of_numbers.append(elem)
    return list_of_numbers



assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]