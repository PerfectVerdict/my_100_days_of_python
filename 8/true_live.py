def calculate_true_love():
    name_one = input("Name one: ")
    name_two = input("Name two: ")
    true = ["t", "r", "u", "e"]
    love = ["l", "o", "v", "e"]
    occurences = 0
    for letter in true:
        if letter in name_one or letter in name_two:
            occurences += 1
    for letter in love:
        if letter in name_one or letter in name_two:
            occurences += 1
    print(f"Your true love score is {occurences}")

calculate_true_love()
