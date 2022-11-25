# # Welcome to the Calculator
#
# new_process = True
# result = 0
#
#
# def divide(number_one, number_two):
#     return number_one / number_two
#
#
# def multiply(number_one, number_two):
#     return number_one * number_two
#
#
# def subract(number_one, number_two):
#     return number_one - number_two
#
#
# def sum(number_one, number_two):
#     return number_one + number_two
#
#
# while new_process:
#
#     process_type = input("Please enter to sum \"+\", to subtract \"-\", to divide \"/\", to multiply \"*\" ")
#     number_one = float(input("Please enter first number: "))
#     number_two = float(input("Please enter second number: "))
#
#     if process_type == "+":
#         result = sum(number_one, number_two)
#         print(f"Result is {result}")
#     elif process_type == "-":
#         result = subract(number_one, number_two)
#         print(f"Result is {result}")
#     elif process_type == "*":
#         result = multiply(number_one, number_two)
#         print(f"Result is {result}")
#     elif process_type == "/":
#         result = divide(number_one, number_two)
#         print(f"Result is {result}")
#     else:
#         print("You entered unacceptable argument!")
#
#     letter = input("Please type \"y\" to keep new process with old result!")
#
#     if letter != "y":
#         new_process = False
#
#
