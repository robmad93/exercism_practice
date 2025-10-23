def leap_year(year):
    # (Divisible by 4 AND NOT divisible by 100) OR (Divisible by 400)
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
