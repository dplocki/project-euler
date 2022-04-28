# https://projecteuler.net/problem=19

MONDAY = 0
SUNDAY = 6
MONTHS_30_DAY_LONG = set([ 4, 6, 9, 11 ])
FEBRUARY = 2

def dates():
    day_of_week = MONDAY
    day_of_month = 1
    month = 1
    year = 1900
    is_leap_year = False

    while not (day_of_month == 1 and month == 1 and year == 2001):
        yield day_of_week, day_of_month, month, year

        day_of_week += 1
        day_of_week %= 7

        day_of_month += 1

        if ((month == FEBRUARY) and ((is_leap_year and day_of_month == 30) or (not is_leap_year and day_of_month == 29))) \
            or (month in MONTHS_30_DAY_LONG and day_of_month == 31) \
            or (day_of_month == 32):

            day_of_month = 1
            month += 1

        if month == 13:
            month = 1
            year += 1
            is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(sum(1
    for day_of_week, day_of_month, _, year in dates()
    if year > 1900 and day_of_week == SUNDAY and day_of_month == 1))
