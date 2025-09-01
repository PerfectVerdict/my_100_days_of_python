from game_data import data
from art import logo


def calculate(score):
    choice = int(input("Who has more followers on Instagram? (1 or 2): "))
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


def try_again():
    another_try = input("Do you want to try again? Type yes or no: ").lower()
    return another_try == "yes"


def play_game(score):
    print(logo)
    print(data[score]["name"])
    print("or")
    print(data[score + 1]["name"])
    correct = calculate(score)  # Only ask once
    if correct:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
    return correct, score  # Return result and updated score


# Main game loop
is_playing = True
score = 0

print("Welcome to Higher or Lower!")

while is_playing:
    correct, score = play_game(score)
    if not correct:
        is_playing = try_again()  # Update loop based on user input
        if is_playing:
            score = 0  # Reset score if they choose to play again
