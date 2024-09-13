from game_data import *
import sys

response = input("Welcome to Higher and Lower. Press a 'Y' to continue. ")
if response != "y" and response != "Y":
    sys.exit()

index = 0
for index in range(len(data)-1):
    print("")
    print("Compare A: {0}, {1}, from {2}".
          format(data[index].get("name"), data[index].get("description"),
                 data[index].get("country")))
    print("Against B: {0}, {1}, from {2}".
          format(data[index+1].get("name"), data[index+1].get("description"),
                 data[index+1].get("country")))

    get_input = True
    continue_game = False
    while get_input:
        response = input("Who has more followers? Please enter A or B. ")
        if response == "a" or response == "A":
            get_input = False
            if data[index].get("follower_count") >= data[index+1].get("follower_count"):
                continue_game = True
        elif response == "b" or response == "B":
            get_input = False
            if data[index].get("follower_count") <= data[index + 1].get("follower_count"):
                continue_game = True

    if not continue_game:
        print("Incorrect answer.")
        break

if index == len(data)-2:
    print("Great.")

print("Your score is {0}".format(index))
