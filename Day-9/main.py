# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
#
# student_grades = {}
#
# for key in student_scores:
#     if 90 < student_scores[key] < 101:
#         student_grades[key] = "Outstanding"
#     elif 80 < student_scores[key] < 91:
#         student_grades[key] = "Exceeds Expectations"
#     elif 70 < student_scores[key] < 81:
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] < 71:
#         student_grades[key] = "Fail"
#     else:
#         print("You entered unacceptable value!")
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
#
# # 🚨 Don't change the code below 👇
# print(student_grades)
#
# travel_log = {
#     "France": ["Paris", "Marsiella", ]
# }
#
# travel_log["France"].append("London")
# print(travel_log)
#
#
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
# def add_new_country(new_country, number_of_visit, city_names):
#     travel_log.append({
#         "country": new_country,
#         "visits": number_of_visit,
#         "cities": city_names
#     })
#
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# people = {}
#
#
# def add_new_user(name, offer):
#     people[name] = offer
#
#
# new_user = "yes"
#
# while True:
#     if new_user == "yes":
#         new_user_name = input("Please enter new users name: \n")
#         new_user_offer = int(input("Please enter your offer: \n"))
#         add_new_user(new_user_name, new_user_offer)
#     else:
#         break
#
#     new_user = input("If you want to enter another user please type 'yes' else press any key and press enter!\n").lower()
#     clear()
#
#
# winner = {
#     "name": "",
#     "offer": 0
# }
#
# for user in people:
#     if people[user] > winner["offer"]:
#         winner["name"] = user
#         winner["offer"] = people[user]
#
# print(f"The winner is {winner['name']} with offer: {winner['offer']}")
