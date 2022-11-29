# Welcome to the Blackjack Game!
import random

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""


def get_card():
    return random.randint(1, 10)


def print_cards(cards, name):
    print(f"{name} cards: {cards}")


def cards_sum(cards):
    sum = 0
    for i in cards:
        sum += i
    return sum


def who_is_winner(user_card, computer_cards):
    user_sum = cards_sum(user_card)
    computer_sum = cards_sum(computer_cards)

    if computer_sum < user_sum < 22 or (user_sum < 22 and computer_sum > 21):
        print("You win")
    elif user_sum < computer_sum < 22 or (computer_sum < 22 and user_sum > 21):
        print("You lose")
    else:
        print("Draw")


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play_game == "y":
    print(logo)
    user_hand = [get_card(), get_card()]
    computer_hand = [get_card(), get_card()]
    print_cards(user_hand, "Your")
    print(f"Computer's first card: {computer_hand[0]}")
    user_hand_sum = cards_sum(user_hand)
    computer_hand_sum = cards_sum(computer_hand)

    while cards_sum(computer_hand) < 18:
        computer_hand.append(get_card())

    user_choice = "y"

    while cards_sum(user_hand) < 22 and user_choice == "y":
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == "y":
            user_hand.append(get_card())
        print(f"Your cards {user_hand}, current score: {cards_sum(user_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

    print(f"Your final hand: {user_hand}, score: {cards_sum(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, score: {cards_sum(computer_hand)}")
    who_is_winner(user_hand, computer_hand)
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
