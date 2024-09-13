import random
from game_data import data

def format_choice(account):
    """Returns a formatted string with the account's details."""
    return f"{account['name']}, a {account['description']} from {account['country']}."

def higher_lower_game():
    score = 0
    game_should_continue = True
    account_a = random.choice(data)
    
    while game_should_continue:
        # Account B should be different from Account A
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"\nCompare A: {format_choice(account_a)}")
        print("VS")
        print(f"Compare B: {format_choice(account_b)}")

        # Ask user to guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check follower counts
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        
        is_correct = (guess == 'a' and a_follower_count > b_follower_count) or (guess == 'b' and b_follower_count > a_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            # Swap account B to A for the next round
            account_a = account_b
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
higher_lower_game()
