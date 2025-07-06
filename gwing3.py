import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_title():
    title = "✦ ROCK • PAPER • SCISSORS ✦"
    for i in range(len(title) + 1):
        print("\033[95m" + title[:i] + "\033[0m", end="\r")
        time.sleep(0.05)
    time.sleep(0.5)
    print("\033[1;44m" + title.center(60) + "\033[0m\n")

def print_background():
    pattern = ["░", "▒", "▓", "█"]
    for _ in range(3):
        line = "".join(random.choice(pattern) for _ in range(60))
        print("\033[90m" + line + "\033[0m")

def rps_game():
    clear()
    animate_title()
    print_background()
    print("\nWelcome to Rock, Paper, Scissors Showdown!\n")
    name = input("Enter your name, Warrior: ")
    print(f"\nHello {name}! First to 3 wins will be crowned the Champion.\n")

    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        print(f"\n{name}: {user_score}  |  Computer: {computer_score}")
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice not in choices:
            print("\033[91mInvalid choice! Try again.\033[0m")
            continue

        computer_choice = random.choice(choices)
        print(f"\nComputer chose: \033[96m{computer_choice}\033[0m")

        if user_choice == computer_choice:
            print("\033[93mIt's a tie!\033[0m")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("\033[92mYou win this round!\033[0m")
            user_score += 1
        else:
            print("\033[91mComputer wins this round!\033[0m")
            computer_score += 1
        time.sleep(1)

    if user_score == 3:
        print(f"\n\033[1;42m {name} is the Champion! 🏆 \033[0m\n")
    else:
        print(f"\n\033[1;41m Computer is the Champion! 💻🏆 \033[0m\n")

    print(f"Final Score ➔ {name}: {user_score} | Computer: {computer_score}\n")
    print("Thanks for playing!\n")

rps_game()
