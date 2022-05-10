import datetime


def get_day(day, is_leap):
    if is_leap:
        year = 2020
    else:
        year = 2021
    leap_year = datetime.datetime(year, 1, 1)
    result = leap_year + datetime.timedelta(days=day - 1)
    date_time = result.strftime("%B, %-d")
    return date_time
