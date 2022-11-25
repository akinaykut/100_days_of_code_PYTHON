# def my_function(name):
#     print(f"My name is {name}")
#
#
# my_function("Akin")
#
# #Write your code below this line 👇
#
# def paint_calc(height, width, cover):
#     result = round((height * width) / cover)
#     print(f"You'll need {result} cans of paint.")
#
#
#
#
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Write your code below this line 👇
# def prime_checker(number):
#     divide = 0
#     for i in range(1, number):
#         if number % i == 0:
#             divide += 1
#     if divide == 1:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# ------------------------------------------

# Caesar Cipher
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
#
#
# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(text, shift):
#     cipher_text = ""
#     for char in text:
#         position = alphabet.index(char)
#         new_position = position - shift
#         cipher_text += alphabet[new_position]
#
#     print(f"The decrypt text is {cipher_text}")
#
#
# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)
#







