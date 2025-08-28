import random

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
art_map = {
    "r": rock_art,
    "p": paper_art,
    "s": scissors_art,
}
choices = ["r", "p", "s"]
random_int = random.randint(0, len(choices) - 1)
computer_choice = choices[random_int]
user_choice = input("Choose r, p, or s: ")
print(f"You chose {user_choice}")
print(art_map[user_choice])
print(computer_choice)
print(art_map[computer_choice])
# Decide winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "r" and computer_choice == "s")
    or (user_choice == "p" and computer_choice == "r")
    or (user_choice == "s" and computer_choice == "p")
):
    print("You win!")
else:
    print("You lose!")
