# Learning how to work w csv and pandas

# import csv 
import pandas

# with open ("./weather_data.csv") as weather_data:
#     # data = weather_data.readlines()
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# data = pandas.read_csv("./weather_data.csv")
# temp = data["temp"]
# print(temp)

# data_dict = data.to_dict()
# data_temp = data.temp
# def average_temp(temp_list):
#     sum = 0
#     for i in temp_list:
#         sum += i
    
#     average = sum // len(temp_list)
#     print(average)

# average_temp(data_temp.tolist())
# print(data_temp.mean())
# print(data_temp.max())

# print(data[data.day == "Wednesday"])
# print(data[data_temp == data_temp.max()])


# students = {
#     "names": ["Ivan","Danylo","Katya"],
#     "scores": [76,40,98]
# }

# student_data = pandas.DataFrame(students)
# student_data.to_csv("new_csv.csv")
# print(student_data)

squirrel_data = pandas.read_csv("./Squirrel_Data.csv")

fur_colour = squirrel_data["Primary Fur Color"]


black = len(squirrel_data[fur_colour == "Black"])
cinnamon = len(squirrel_data[fur_colour == "Cinnamon"])
grey = len(squirrel_data[fur_colour == "Gray"])

squirrel_dict = {
    "Fur Colour": ["Black", "Cinnamon", "Grey"],
    "Count": [black,cinnamon,grey]
}

new_data = pandas.DataFrame(squirrel_dict)
new_data.to_csv("Squirrel_Count.csv")
