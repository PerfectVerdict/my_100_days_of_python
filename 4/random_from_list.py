import random

friends = ["alice", "joana", "bob"]
num_of_friends = len(friends)
random_int = random.randint(0, num_of_friends - 1)
random_choice = friends[random_int]

print(random_choice)
