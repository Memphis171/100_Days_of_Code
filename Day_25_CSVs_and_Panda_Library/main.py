# # # Using csv to read the lines in the csv file weather data
# # # import csv
# # # with open("weather_data.csv")as file:
# # #     data = csv.reader(file)
# # #     temperatures = []
# # #     for row in data:
# # #         if row[1] != 'temp':
# # #             temperatures.append(float(row[1]))
# # #         else:
# # #             pass
# # #     print(temperatures)
# #
# #
# # #doing the same but using the pandas library
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# temperatures = data["temp"]
# # print(temperatures)
# #
# # #getting stats on the data
# # print(temperatures.mean())
# # print(temperatures.max())
# #
# # # getting a row instead of a column (series)
# #
# # print(data[data.day == 'Monday'])
# # print(data[data.temp == temperatures.max()])
# #
# # #
# Monday = data[data.day == 'Monday']
# f_temp = Monday.temp[0]*(9/5)+32
# print(f_temp)
import csv

#take the data from the central park squirrel census data and create a new csv
import pandas as pd
with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251014.csv") as file:
    squirrel_file = pd.read_csv(file)
    # gray_list = squirrel_file[squirrel_file["Primary Fur Color"] == "Gray"]
    # cin_list = squirrel_file[squirrel_file["Primary Fur Color"] == "Cinnamon"]
    # black_list = squirrel_file[squirrel_file["Primary Fur Color"] == "Black"]
    # print(type(gray_list))
    squirrel_count = pd.DataFrame(squirrel_file["Primary Fur Color"].value_counts())
    squirrel_count.to_csv("squirrel_count.csv")