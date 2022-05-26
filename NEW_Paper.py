import random

while True:
    player_try = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {player_try}, computer chose {computer_action}.\n")

    if player_try == computer_action:
        print(f"Both players selected {player_try}. Amazing it's a tie!")
    elif player_try == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_try == "paper":
        if computer_action == "rock":
            print("Paper covers rock! Congrats, You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_try == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Want to Play again? Type y to play again or n to end the game now (y/n): ")
    #
    if play_again.lower() != "y":
        break