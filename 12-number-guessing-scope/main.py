import random


def choose_difficulty():
    diff = input("Do you want easy or hard mode (easy/hard): ").lower()
    return 10 if diff == "easy" else 5


def play_game():
    chances = choose_difficulty()
    target_number = random.randint(1, 100)  # new number each round
    print("\nI'm thinking of a number between 1 and 100.")

    while chances > 0:
        guess = int(input(f"Guess a number ({chances} tries left): "))
        if guess == target_number:
            print(f"You got it! The number was {target_number}")
            break
        elif guess < target_number:
            print("Too low")
        else:
            print("Too high")
        chances -= 1

    if chances == 0:
        print(f"You ran out of chances. The number was {target_number}")


def try_again():
    again = input("Do you want to play again? (yes/no): ").lower()
    return again == "yes"


# Main game loop
playing = True
print("Welcome to the number guessing game!")
while playing:
    play_game()
    playing = try_again()
    print("\n" * 40)
