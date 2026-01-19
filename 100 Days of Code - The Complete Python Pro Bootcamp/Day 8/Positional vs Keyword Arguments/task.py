# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}?")


# greet_with_name("Scuba Steve", "Atlantis")

def calculate_love_score(name1, name2):
    true = 0
    love = 0
    name = name1 + name2

    for letter in name.lower():
        if letter == "t":
            true += 1
        if letter == "r":
            true += 1
        if letter == "u":
            true += 1
        if letter == "e":
            true += 1

    for letter in name.lower():
        if letter == "l":
            love += 1
        if letter == "o":
            love += 1
        if letter == "v":
            love += 1
        if letter == "e":
            love += 1

    print(f"Your love score is: {true}{love}")

calculate_love_score("Scuba Steve", "Sisyphus")