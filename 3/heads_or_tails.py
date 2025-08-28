import random

random_int = random.randint(1, 2)
print(random_int)
if random_int % 2 == 1:
    print("Heads")
elif random_int % 2 == 0:
    print("tails")
