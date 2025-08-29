def is_leap_year(year):
    if year % 4 != 0:
        return "Not a leap year"
    elif year % 100 != 0:
        return "A leap year"
    elif year % 400 != 0:
        return "Not a leap year"
    else:
        return "A leap year"

year = int(input("What year to check: "))
print(is_leap_year(year))

