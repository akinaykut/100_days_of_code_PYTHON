# # Hangman Game
#
# # Step 1
#
# import random
#
# word_list = ["aardvark", "baboon", "camel"]
#
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#
#
# def create_blank_word(data):
#     new_word = []
#     for char in data:
#         new_word.append("_")
#
#     return new_word
#
#
# def get_users_guess():
#     char = input("Please enter a character: ")
#
#     char = char.lower()
#
#     return char
#
#
# def check_the_guess(char):
#     for i in word:
#         if i == char:
#             return True
#
#
# def print_users_guess(char, users_list, word):
#     for i in range(0, len(word)):
#         if word[i] == char:
#             users_list[i] = char
#
#     return users_list
#
#
# def check_is_user_win(data):
#     for char in data:
#         if char == "_":
#             return False
#     return True
#
#
# word = random.choice(word_list)
# users_word = create_blank_word(word)
# heal = 5
#
# while heal > 0:
#
#     if check_is_user_win(users_word):
#         print("You Win!")
#         break
#
#     users_char = get_users_guess()
#     if check_the_guess(users_char):
#         users_word = print_users_guess(users_char, users_word, word)
#         users_word_string = ''.join(users_word)
#         print(users_word_string)
#     else:
#         print("Wrong guess.")
#         heal -= 1
#         if heal == 0:
#             print("You died.")
