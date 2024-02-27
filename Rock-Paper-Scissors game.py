import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("\nWelcome to Rock, Paper, Scissors Game!")
        print("Enter your choice (rock, paper, or scissors) or 'quit' to exit.")
        user_choice = input("Your choice: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing Better Luck Next Time!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
