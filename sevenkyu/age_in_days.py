import datetime


def age_in_days(year, month, day):
    a_date = datetime.datetime(year, month, day)
    current_day = datetime.datetime.now()
    result = current_day - a_date
    return f'You are {result.days} days old'
