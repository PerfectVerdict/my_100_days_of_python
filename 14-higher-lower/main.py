from game_data import data
from art import logo


""" returns True if they want to keep playing after losing """


def try_again():
    again = input("Do you want to play again? (yes/no): ").lower()
    return again == "yes"


""" returns True if they got it right. False if not """


def calculate(score):
    choice = int(input("Who has more fallowers on instagram?: "))
    if (
        data[score]["follower_count"] > data[score + 1]["follower_count"]
        and choice == 1
    ):
        return True
    elif (
        data[score]["follower_count"] < data[score + 1]["follower_count"]
        and choice == 2
    ):
        return True
    else:
        return False


score = 0


def advance_the_question(score):
    score += 1
    return data[score + 1]["name"]


def play_game(score):
    print(logo)
    print(data[score]["name"])
    print("or")
    print(data[score + 1]["name"])
    if calculate(score):  # If they got it right:
        print("------------------------------------------")
        print(advance_the_question(score - 1))
        print("or")
        print(advance_the_question(score))
    else:
        print("wrong")

    playing = try_again()
    print("\n" * 40)

    print("Welcome to higher or lower!")


play_game(score)
