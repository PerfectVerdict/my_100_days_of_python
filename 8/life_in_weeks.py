def life_in_weeks(age):
    years_left = 100 - age
    weeks_left = years_left*52
    print(weeks_left)
users_age = int(input("What is your age"))
life_in_weeks(users_age)
