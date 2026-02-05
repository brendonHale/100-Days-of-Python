import random
import pandas

# List Comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Scuba Steve"
letters_list = [letter for letter in name]

range_list = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
uppercase_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
# {new_key:new_value for item in list}
students_score = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_score.items() if score >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp * 9/5 + 32) for (day, temp) in weather_c.items()}

# ---------------------------------

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    # print(key)
    # print(value)
    pass

# Loop through a data frame
student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)