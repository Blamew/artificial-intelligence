# Programmer: Brysom LaMew
# Date: 2.29.24
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")

import random


def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    while True:
        try:
            # Ask the user to guess the number
            guess = int(input("Guess the number between 1 and 100: "))

            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the number.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")


# Call the function to start the game
guess_number()