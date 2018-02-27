# return if year is leap


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

# check if dates is valid


def is_valid(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    else:
        if month2 > month1:
            return True
        else:
            if day2 > day1:
                return True
    return False


# return the next day


def next_day(year1, month1, day1):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month1 == 2 and is_leap(year1):
        months[1] = 29
    if day1 < months[month1-1]:
        day1 = day1 + 1
    else:
        day1 = 1
        month1 = month1 + 1
    if month1 > 12:
        month1 = 1
        year1 = year1 + 1
    return year1, month1, day1


def days_of_life(year1, month1, day1, year2, month2, day2):
    total_days = 0
    while is_valid(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        total_days = total_days + 1
    return total_days


print(days_of_life(1994, 6, 25, 2018, 2, 27))
