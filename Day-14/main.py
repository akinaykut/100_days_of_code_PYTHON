import art
import data
import random

answer = True
score = 0
while answer:

    print(art.logo)
    if score == 0:
        first_pick = random.choice(data.data)
    else:
        first_pick = second_pick

    second_pick = random.choice(data.data)

    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {first_pick['name']}, {first_pick['description']}, from {first_pick['country']} ")

    print(art.vs)

    if first_pick == second_pick:
        second_pick = random.choice(data.data)

    print(f"Against B: {second_pick['name']}, {second_pick['description']}, from {second_pick['country']} ")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if first_pick['follower_count'] > second_pick['follower_count'] and user_answer == "a":
        score += 1
    elif second_pick['follower_count'] > first_pick['follower_count'] and user_answer == "b":
        score += 1
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        answer = False

