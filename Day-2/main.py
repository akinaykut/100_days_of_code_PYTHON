# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# # Write your code below this line 👇
#
# first_number = int(two_digit_number[0])
# second_number = int(two_digit_number[-1])
# print(first_number + second_number)


# number = input("enter a number:")
#
# print(int(number) % 10 + int(int(number)/10))

# --------------------------------------------


# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# age = int(age)
# months = age * 12
# weeks = age * 52
# days = age * 365
#
# months_1 = (90 * 12) - months
# days_1 = (90 * 365) - days
# weeks_1 = (90 * 52) - weeks
#
#
# print(f"You have {days_1} days, {weeks_1} weeks, and {months_1} months left.")



#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# print("Welcome to the tip calculator!")
#
# bill = float(input("Please enter your bill: $"))
# number_of_person = int(input("Please enter number of person: "))
# tip = int(input("Please enter percent of tip: "))
#
# bill_with_tip = (bill / 100) * tip + bill
# result = bill_with_tip / number_of_person
# result = "{:.2f}".format(result)
#
# print(f"Each person should pay ${result}")
