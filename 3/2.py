from datetime import datetime


def get_days_from_today(date='2024-06-22'):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        cur_date = datetime.today().date()
        return (cur_date - date).days
    except:
        print('Date must be YYYY-MM-DD')
get_days_from_today()

