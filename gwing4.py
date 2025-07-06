import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_title():
    title = "✦ THE FORGOTTEN QUEST ✦"
    for i in range(len(title) + 1):
        print("\033[95m" + title[:i] + "\033[0m", end="\r")
        time.sleep(0.05)
    time.sleep(0.5)
    print("\033[1;44m" + title.center(60) + "\033[0m\n")

def start_story():
    clear()
    animate_title()
    print("\nYou awaken in a dark forest, the air thick with mist.")
    print("A torn map lies beside you, marked with a single word: ESCAPE.\n")
    time.sleep(2)
    choice1 = input("Do you: \n1. Follow the old path\n2. Enter the dark cave\n\nType 1 or 2: ")

    if choice1 == '1':
        path_route()
    elif choice1 == '2':
        cave_route()
    else:
        print("\n\033[91mInvalid choice. The forest swallows you whole.\033[0m\n")
        time.sleep(2)

def path_route():
    print("\nYou walk along the path. Strange whispers echo around you.")
    time.sleep(2)
    choice2 = input("\nDo you: \n1. Run towards the sound\n2. Stay silent and hide\n\nType 1 or 2: ")

    if choice2 == '1':
        print("\nA pack of shadow wolves leaps out. You are devoured.\n\033[91mGAME OVER\033[0m\n")
    elif choice2 == '2':
        print("\nThe whispers fade. You find an ancient key buried in the soil.")
        time.sleep(2)
        print("\nUsing the key, you unlock a hidden gate leading to the sunrise.\n\033[92mYOU ESCAPED!\033[0m\n")
    else:
        print("\n\033[91mConfused, you freeze. The forest claims you.\033[0m\n")

def cave_route():
    print("\nYou enter the cave. The air grows cold. Eyes watch you from the darkness.")
    time.sleep(2)
    choice3 = input("\nDo you: \n1. Light a torch\n2. Walk blindly\n\nType 1 or 2: ")

    if choice3 == '1':
        print("\nThe torchlight reveals a treasure chest.")
        time.sleep(2)
        choice4 = input("\nDo you: \n1. Open the chest\n2. Leave it alone\n\nType 1 or 2: ")
        if choice4 == '1':
            print("\nThe chest contains a glowing stone. A portal opens.")
            time.sleep(2)
            print("\nYou step through and escape the cursed forest.\n\033[92mYOU ESCAPED!\033[0m\n")
        elif choice4 == '2':
            print("\nThe chest explodes in the dark. Your journey ends here.\n\033[91mGAME OVER\033[0m\n")
        else:
            print("\n\033[91mTime runs out. The cave collapses.\033[0m\n")
    elif choice3 == '2':
        print("\nYou stumble and fall into an endless abyss.\n\033[91mGAME OVER\033[0m\n")
    else:
        print("\n\033[91mThe cave seals behind you. Forever trapped.\033[0m\n")

start_story()
