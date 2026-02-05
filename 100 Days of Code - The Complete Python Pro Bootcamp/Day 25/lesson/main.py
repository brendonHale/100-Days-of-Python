# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# # average = sum(temp_list) / len(temp_list)
# average = data["temp"].mean()
# max = data["temp"].max()
#
# # print(data["condition"])
# # print(data.condition)
#
# # Get data in Row
# # print(data[data.day == "Monday"])
#
# # Get row with the highest temp
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday.temp * (9/5) + 32
#
# # Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")