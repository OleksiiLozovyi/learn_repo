from typing import Callable, Generator
import re



def generator_numbers(text: str) -> Callable:
    num_list = re.findall(r" \d+.\d+ ", text, re.MULTILINE)
    for num in num_list:
        yield num


def sum_profit(text: str, func: Callable[[str], Generator]) -> float:
    sum_num = 0
    for num in func(text):
        sum_num += float(num)
    return sum_num

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")