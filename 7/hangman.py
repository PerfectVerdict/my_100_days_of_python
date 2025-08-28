import random

from words import word_list
from art import stages, logo
lives = 6
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
guessed_incorrectly = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You have {lives} lives left.")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You already guessed that correctly.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
# If they guessed an incorrect one already, don't deduct a life.
    if guess not in chosen_word:
        if guess not in guessed_incorrectly:
            guessed_incorrectly.append(guess)
            print(f"{guess} is incorrect.")
            lives -= 1
        elif guess in guessed_incorrectly:
            print(f"You already guessed {guess}.")
        if lives != 0:
            print(stages[lives])
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(f"You lost. The correct work was {chosen_word}")
            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.


    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py


