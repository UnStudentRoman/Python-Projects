#
# file_1_list = []
# file_2_list = []
#
#
# with open("file_1.txt") as file_1:
#     file_1 = file_1.readlines()
#     for number in file_1:
#         number = number.strip()
#         file_1_list.append(int(number))
#
# with open("file_2.txt") as file_2:
#     file_2 = file_2.readlines()
#     for number in file_2:
#         number = number.strip()
#         file_2_list.append(int(number))
#
#
# print(file_1_list)
# print(file_2_list)
#
# result = [number for number in file_1_list if number in file_2_list]
# print(result)

# sentence = "What is the Airspeed Velocity of an Unlanded Swallow?"
#
# dict_sentence = [word for word in sentence.split()]
#
# final_dict = {word:len(word) for word in sentence.split()}
#
# print(type(final_dict))
# print(final_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp_c*9/5) + 32) for (day,temp_c) in weather_c.items()}

print(weather_f)
