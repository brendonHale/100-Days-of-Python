# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("data/my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# with open("new_file.txt") as file:
#     file.write("This will create a new folder")
