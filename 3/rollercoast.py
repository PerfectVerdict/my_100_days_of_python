height = input("Is your height over 120cm? ")

if height == "y":
    bill = 0
    age = int(input("How old are you?"))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 12
    elif age >= 45 and age <= 55:
        print("Have a free ticket on us")

    else:
        bill += 7

    wants_pic = input("Do you want a picture? ")
    if wants_pic == "y":
        bill += 3
        print(f"Your total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")


else:
    print("You can't ride.")
