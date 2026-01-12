import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# friend = random.choice(friends)
# print(friend)

friend = random.randint(0, len(friends) - 1)
print(friends[friend])