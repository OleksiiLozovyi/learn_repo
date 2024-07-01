def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n=4, k=3):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))
print(number_of_groups())
