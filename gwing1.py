import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_title():
    title = "★ RIDDLE RUSH QUEST ★"
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

def intro():
    clear()
    print_background()
    print()
    name = input("\033[96mEnter your adventurer name: \033[0m")
    print(f"\nWelcome, \033[1;35m{name}\033[0m, to the realm of numbers...")
    print("Your fate lies in five riddles. Solve them or fade into the unknown.\n")
    time.sleep(2)
    return name

def game_over_screen(score, name, high_score):
    clear()
    print("\n\033[1;45m GAME OVER \033[0m\n")
    trophy = """
        .-=========-.
        \\'-=======-'/ 
        _|   .=.   |_
       ((|  {{1}}  |))
        \|   /|\   |/
         \__ '`' __/
           _`) (`_
         _/_______\_
        /___________\\
    """
    print("\033[93m" + trophy + "\033[0m")
    print(f"\n\033[1m{name}'s Final Score: {score}/5\033[0m")
    if score == 5:
        print("\033[96m👑 Perfect! You are the Riddle Master!\033[0m")
    elif score >= 3:
        print("\033[94m⚡ Brave attempt! Well done.\033[0m")
    else:
        print("\033[90m...The riddles have defeated you.\033[0m")
    print(f"\n🏆 High Score: {high_score}\n")
    time.sleep(3)

def save_high_score(score):
    try:
        with open('highscore.txt', 'r') as f:
            high_score = int(f.read().strip())
    except:
        high_score = 0
    if score > high_score:
        with open('highscore.txt', 'w') as f:
            f.write(str(score))
        high_score = score
    return high_score

def play_game():
    player = intro()
    animate_title()
    print_background()
    time.sleep(1)
    print("\nYour quest begins...\n")
    time.sleep(1)

    score = 0
    levels = [
        ("Easy", [("Guess between 1 and 5", random.randint(1,5))]),
        ("Medium", [("Find the number between 10 and 20", random.randint(10,20))]),
        ("Hard", [("Name the shadow digit 50 to 60", random.randint(50,60))]),
        ("Bonus", [("Reveal the magic code 100 to 105", random.randint(100,105))]),
        ("Final", [("Unseal the gate 200 to 205", random.randint(200,205))])
    ]

    for lvl, qs in levels:
        print(f"\n\033[1;30;46m Level: {lvl} \033[0m\n")
        for q, a in qs:
            print(q)
            start = time.time()
            try:
                guess = int(input("→ Your guess: "))
                elapsed = time.time() - start
                if guess == a:
                    print("\033[92m✓ Correct!\033[0m")
                    if elapsed < 5:
                        print("\033[96m⏱ Speed Bonus!\033[0m")
                        score += 2
                    else:
                        score += 1
                else:
                    print(f"\033[91m✗ Missed! It was {a}\033[0m")
            except:
                print("\033[93m⚠ Invalid!\033[0m")
            time.sleep(1)

    high_score = save_high_score(score)
    game_over_screen(score, player, high_score)

play_game()
