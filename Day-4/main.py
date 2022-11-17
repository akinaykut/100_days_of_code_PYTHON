# ----------------------------------------
# import my_module
# import random
#
# random_number = random.random() * 5
#
# fruits = ["Apple", "Grape", 5, True, False, "25", 707, [5, 6, "15", False]]
#
#
# print(random_number)
# print("Hello World!")
# my_module.print_my_name("akin")
#
# ----------------------------------------

# # Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
#
# names_count = len(names)
# lucky_man = names[random.randint(0, names_count)]
#
# print(f"{lucky_man} is going to buy the meal today!")

# ----------------------------------------


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# column = int(position[0]) - 1
# row = int(position[1]) - 1
#
# map[row][column] = "X"
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# ----------------------------------------

# # Rock
# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# # Paper
# paper = '''
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# # Scissors
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
#
# def print_symbol(number):
#     if number == 0:
#         print(rock)
#     elif number == 1:
#         print(paper)
#     else:
#         print(scissors)
#
#
# print("Welcome to the Rock, Paper, Scissors Game! ")
#
# users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))
# computers_choice = random.randint(0, 2)
#
# print("Your choice: ")
# print_symbol(users_choice)
# print("Computers choice: ")
# print_symbol(computers_choice)
#
# if users_choice == 0:
#     if computers_choice == 1:
#         print("You lose.")
#     elif computers_choice == 2:
#         print("You win.")
#     else:
#         print("Draw")
# elif users_choice == 1:
#     if computers_choice == 0:
#         print("You win.")
#     elif computers_choice == 1:
#         print("Draw")
#     else:
#         print("You lose.")
# else:
#     if computers_choice == 0:
#         print("You lose.")
#     elif computers_choice == 1:
#         print("You win")
#     else:
#         print("Draw")
#


