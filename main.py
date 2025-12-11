import json
import os
from colorama import Fore, init, Style

init()

def terminal_clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():

    # Load json file
    try:
        with open("data/spells.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The file 'spells.json' was not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return

    end_number = len(data)

    while True:
        
        terminal_clear()  # <-- clear ONLY here, before showing the main menu

        print(Fore.GREEN + "\n===== VIM SPELL BOOK =====\n")
        print("[1] Start of Line")
        print("[2] End of Line")
        print("[3] Move Cursor")
        print("[4] Jump by Word")
        print("[5] Jump Back by Word")
        print("[6] Top of File")
        print("[7] Bottom of File")
        print("[8] Jump between open and close brackets")
        user_input = input(
            Style.RESET_ALL + f"Enter a number 1-{end_number} or 'q' to quit: "
        ).strip()

        if user_input.lower() == "q":
            print("We vanish in the shadows...")
            break

        try:
            spell_number = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            input("Press Enter to continue...")
            continue
        
        if spell_number < 1 or spell_number > end_number:
            print(f"Number is out of range, please enter a number between 1-{end_number}.")
            input("Press Enter to continue...")
            continue

        selected_spell = data[spell_number - 1]
        
        print(Fore.GREEN)
        print("┌─────────────┐")
        print("│ SPELL INFO  │")
        print("└─────────────┘")

        print(Fore.RED + f"[{spell_number}]")
        print(Style.RESET_ALL + f"{Fore.CYAN}Spell:{Style.RESET_ALL} {selected_spell['name']}")
        print(f"{Fore.CYAN}Command:{Style.RESET_ALL} {selected_spell['command']}")
        print(f"{Fore.CYAN}School:{Style.RESET_ALL} {selected_spell['school']}")
        print(f"{Fore.CYAN}Level:{Style.RESET_ALL} {selected_spell['level']}")
        print(f"{Fore.CYAN}Incantation:{Style.RESET_ALL} {selected_spell['incantation']}") 
        print(Fore.GREEN + "\n==========================")
        print(Style.RESET_ALL)

        input("Press Enter to return to the spellbook...")

        # DO NOT clear here — clearing happens naturally at top of next loop


if __name__ == "__main__":
    main()

