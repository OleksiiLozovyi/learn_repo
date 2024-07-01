from datetime import datetime

def get_days():
    user_input = input('Input: ')
    user_date = datetime.strptime(user_input, '%m')
    print(user_date)
