import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_win_count = 0
    computer_win_count = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.\n")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_win_count += 1
        elif result == "Computer wins!":
            computer_win_count += 1

        print(f"Your current win count: {user_win_count}")
        print(f"Computer's current win count: {computer_win_count}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

    print("\nFinal Scores:")
    print(f"Your total win count: {user_win_count}")
    print(f"Computer's total win count: {computer_win_count}")

if __name__ == "__main__":
    play_game()
