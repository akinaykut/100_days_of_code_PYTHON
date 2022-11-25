# # Welcome to the number guessing game
# import random
#
#
# def game():
#     print("Welcome to The Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     heal = 0
#     if level == "easy":
#         heal = 10
#     else:
#         heal = 5
#
#     answer = random.randint(1, 100)
#
#     while heal > 0:
#         print(f"You have {heal} attemps remaining to guess number.")
#         users_number = int(input("Make a guess: "))
#         if users_number == answer:
#             print("You win")
#             break
#         elif users_number < answer:
#             print("Too high")
#             heal -= 1
#         else:
#             print("Too low")
#             heal -= 1
#         if heal == 0:
#             print("You lose")
#             print(f"The answer was {answer}")
#             if input("\nIf you want to play again, press 'y': ") == "y":
#                 game()
#
#
# game()
