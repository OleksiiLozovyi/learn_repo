from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, target_weekday=0):
    current_weekday = start_date.weekday()
    days_ahead = (target_weekday - current_weekday + 7) % 7
    if days_ahead == 0:
        days_ahead = 7
    next_date = start_date + timedelta(days=days_ahead)
    return next_date

start_date = string_to_date("2024.03.26")  # Перетворення рядка на дату
next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
print(next_monday)
next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(next_friday)