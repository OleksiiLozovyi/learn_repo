from datetime import datetime


def get_days_from_today(date='2024-06-22'):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    cur_date = datetime.today().date()
    print((cur_date - date).days)
get_days_from_today()
