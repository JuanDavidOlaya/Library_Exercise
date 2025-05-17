import os
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def show_menu(options, header):

    title = header

    max_width = max(len(option) for option in options)
    total_width = max(len(title), max_width) + 6

    print(CYAN + "╔" + "═" * total_width + "╗" + RESET)
    print(CYAN + "║" + RESET + title.center(total_width) + CYAN + "║" + RESET)
    print(CYAN + "╠" + "═" * total_width + "╣" + RESET)

    for option in options:
        print(CYAN + "║" + RESET + "  " + GREEN + option.ljust(total_width - 2) + RESET + CYAN + "║" + RESET)

    print(CYAN + "╚" + "═" * total_width + "╝" + RESET)

def try_again(message, alert):
    while True:
        try:
            again = input(MAGENTA + message + RESET).lower()
            if again == 'y':
                 return True
            elif again == 'n':
                return False
            else:
                print(RED + alert + RESET)
        except ValueError:
            print(RED + "Invalid input!" + RESET)