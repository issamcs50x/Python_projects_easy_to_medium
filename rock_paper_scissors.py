from random import choice

GAME_CHOICES = ("r", "p", "s")
EMOJIS = ("🧱", "📄", "✂")
VISUALS = dict(zip(GAME_CHOICES, EMOJIS))

WINNING_CASES = ("rs", "pr", "sp")

def main():
    # keep running until the user quit
    while True:
        # generate a random choise
        com_choice = choice(GAME_CHOICES)
        # ask the user for his choice
        user_choice = input("Rock, Paper or Scissors? (r/p/s): ").strip().lower()
        # Verify that the user has selected from the provided options.
        if user_choice in GAME_CHOICES:
            result = referee(user_choice, com_choice)
            # print results
            show_result(user_choice, com_choice, result)
            # Asking the user about their preference
            answer = input("Continue? (y/n): ").strip().lower()
            if answer == "n":
                break
        # print an error message otherwise
        else:
            print("Invalid choice!")

def referee(user_choice, com_choice):
    # Determining the winner based on game logic 
    # Draw
    if user_choice == com_choice:
        result = "Draw"
    # Win
    elif (user_choice + com_choice) in WINNING_CASES:
        result = "You win!"
    # Lose
    else:
        result = "You lose!"
    return result

def show_result(user_choice, com_choice, result):
    print(f"""
You chose '{VISUALS[user_choice]}'
Computer chose '{VISUALS[com_choice]}'
{result}""")

main()