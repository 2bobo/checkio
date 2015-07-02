def days_diff(date1, date2):
    from datetime import date, timedelta

    start_y, start_m, start_d = date1
    end_y, end_m, end_d = date2
    start_date = date(start_y, start_m, start_d)
    end_date = date(end_y, end_m, end_d)

    days = end_date - start_date
    return abs(days.days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
