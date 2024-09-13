from game_data import *
import sys
import random

# Confirm with user to continue.
response = input("Welcome to Higher and Lower. Press a 'Y' to continue. Else exist. ")
if response != "y" and response != "Y":
    sys.exit()

# Go through each question in the list.
question_count = 0
continue_game = True
first_set = random.choice(data)
second_set = first_set
while continue_game:
    # Read information.
    while first_set == second_set:
        second_set = random.choice(data)

    # Show the question.
    print("")
    print("Compare A: {0}, {1}, from {2}".
          format(first_set.get("name"), first_set.get("description"),
                 first_set.get("country")))
    print("Against B: {0}, {1}, from {2}".
          format(second_set.get("name"), second_set.get("description"),
                 second_set.get("country")))

    # Get user's answer and continue till A or B is entered.
    get_input = True
    response = ""
    while get_input:
        response = input("Who has more followers? Please enter A or B. ")
        if response in ["a", "A", "b", "B"]:
            get_input = False

    # Check if user's answer is correct.
    answer = "a" if first_set.get("follower_count") >= second_set.get("follower_count") else "b"
    if response.lower() == answer:
        continue_game = True
        question_count = question_count + 1
        first_set = second_set
    else:
        print("Incorrect answer.")
        continue_game = False

# Print the score.
print("Your score is {0}".format(question_count))
