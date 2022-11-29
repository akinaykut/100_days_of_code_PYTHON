# Day-3
#
# ------------------------------------------------
#
#
# Odd and Even numbers


print("Welcome to the App!")


number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Your number is Even.")
else:
    print("Your number is Odd.")


# ------------------------------------------------
#
#
# BMI calculator 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height ** 2)

result = round(bmi)


if bmi < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")

#
# ------------------------------------------------
#
# Leap year

print("Welcome to the Leap year Calculator!")

year = int(input("Please enter a year: "))


if year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")


# ------------------------------------------------
#
#
# Pizza Order

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

if size == 'S':
    bill += 15

elif size == 'M':
    bill += 20

else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")

# ------------------------------------------------
#
# Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def count_character(name1, name2, char):
    count = 0
    count += name1.count(char)
    count += name2.count(char)
    return count


def calculate_true_love(name1, name2):

    number1 = 0
    number2 = 0

    number1 += count_character(name1, name2, 't')
    number1 += count_character(name1, name2, 'r')
    number1 += count_character(name1, name2, 'u')
    number1 += count_character(name1, name2, 'e')

    number2 += count_character(name1, name2, 'l')
    number2 += count_character(name1, name2, 'o')
    number2 += count_character(name1, name2, 'v')
    number2 += count_character(name1, name2, 'e')

    number1 = str(number1)
    number2 = str(number2)

    result = number1 + number2
    result = int(result)
    return result


name1 = name1.lower()
name2 = name2.lower()

score = calculate_true_love(name1, name2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")


# ------------------------------------------------
#
# Treasure Island

print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************


''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

data = input("You're at the cross road. Where do you want to go? Type \"left\" or \"right\" \n")
if data == 'left':
    boat = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait a boat."
                 "Type \"swim\" to swim across. \n")

    if boat == "wait":
        door = input("You arrived at the island unharmed. There is a house with 3 doors. "
                     "One red, one yellow and one blue. Which colour do you choose? \n")
        if door == "yellow":
            print("You find the treasure.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")

else:
    print("Game Over.")


# ------------------------------------------------
