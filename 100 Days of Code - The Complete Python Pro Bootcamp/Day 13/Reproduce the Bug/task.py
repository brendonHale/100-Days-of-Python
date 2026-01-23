from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# Array indexing starts at 0, and goes until N - 1
# dice_num should be: randint(0, 6)
print(dice_images[dice_num])
