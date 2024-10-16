# Project 1: 'Snake', 'Water', 'Gun'

import random

# Step 0: Welcome message and introduction of game
print("Welcome to 'Snake', 'Water', 'Gun' game!")
choices = ['Snake', 'Water', 'Gun']
print(f" Select from {choices}")

while True:
    # Step 1: Get user input with validation
    MAX_ATTEMPTS = 3
    attempts = 0
    user_choice = None

    while attempts <= MAX_ATTEMPTS:
        user_choice = input("Enter your choice: ").capitalize() # Use capitalize to standardize input
        if user_choice in choices:
            break # Exit the loop if choice is valid
        else:
            attempts +=1
            print(f"Invalid choice! You have {MAX_ATTEMPTS - attempts} attempts left out of {MAX_ATTEMPTS}, Kindly choose from {choices}")
    if attempts == MAX_ATTEMPTS:
        print(f"Too many invalid attempts! Default choice 'Snake' will be used")
        user_choice = 'snake'

    # Step 2: Generate computer's choice
    computer_choice = random.choice(choices)

    # Step 3: Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Snake' and computer_choice == 'Gun') or \
         (user_choice == 'Gun' and computer_choice == 'Water') or \
         (user_choice == 'Water' and computer_choice == 'Snake'):
        result = "Wow, You win"
    else:
        result = "Computer wins!"

    # Display the result
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

    # Step 4: If user wants to play game again.
    Play_again = input(f"Do you want to play again, type 'Yes'/'No': ").lower()
    if Play_again != 'yes':
        print("Thanks for playing the game! Come again!")
        break # Exit the loop
