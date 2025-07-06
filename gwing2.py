import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_title():
    title = "★ GUESS THE NUMBER ★"
    for i in range(len(title) + 1):
        print("\033[95m" + title[:i] + "\033[0m", end="\r")
        time.sleep(0.05)
    time.sleep(0.5)
    print("\033[1;44m" + title.center(50) + "\033[0m\n")

def print_background():
    pattern = ["░", "▒", "▓", "█"]
    for _ in range(5):
        line = "".join(random.choice(pattern) for _ in range(50))
        print("\033[90m" + line + "\033[0m")

def number_guess_game():
    clear()
    animate_title()
    print_background()
    print("\nWelcome to the Number Guessing Game!")
    name = input("\nEnter your name, Challenger: ")
    print(f"\nHello {name}! I have chosen a number between 1 and 50.")
    print("You have 7 attempts to guess it. Let the challenge begin!\n")

    secret_number = random.randint(1, 50)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input(f"Guess the number (Attempts left: {attempts}): "))
            if guess == secret_number:
                print("\033[92m✓ Congratulations! You guessed it right!\033[0m")
                break
            elif guess < secret_number:
                print("\033[94m➔ Too Low!\033[0m")
            else:
                print("\033[93m➔ Too High!\033[0m")
            attempts -= 1
        except:
            print("\033[91mInvalid input! Enter a number.\033[0m")

        time.sleep(0.5)

    if attempts == 0:
        print(f"\n\033[91m✗ Game Over! The correct number was {secret_number}.\033[0m")
    else:
        print(f"\n\033[96m★ Well done, {name}! You did it in {7 - attempts + 1} attempt(s).\033[0m")

    print("\nThank you for playing!\n")

number_guess_game()
