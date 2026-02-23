# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error:
#     print(f"The key {error} does not exist")
# else:
#     # Triggers if the Try block succeeds
#     content = file.read()
#     print(content)
# finally:
#     # Always runs
#     file.close()
#     raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be over 3m")

bmi = weight / height ** 2
print(bmi)

# ----------------------------------- #

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)