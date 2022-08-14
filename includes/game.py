from os import system, name


def clear_screen():  # Clears the Screen
    system("clear")
    # if name == "nt":
    #     system("cls")
    # else:
    #     system("clear")


def show_title(name):  # Shows the Game's title in uppercase
    print(name.upper())
    print("")


def show_main_menu():  # Shows the possible options in a game
    print("1. New Game")
    print("2. Options")
    print("3. Quit")


def print_player_data(path):  # Prints the player data
    player_data = open(path, "r")
    if player_data.readable():
        print(player_data.read())
    player_data.close()


def save_player_data(path):  # Saves the local data to player file
    player_data = open(path, "r")
    new_data = open(path + ".backup", "w")
    if player_data.readable():
        for data in player_data.readlines():
            new_data.write(data)
    new_data.close()
    player_data.close()


def show_game():  # Runs the game window
    print("Game Started!")
    print("")
    print_player_data("data/player.txt")
    to_run = True
    while to_run:
        print("1. Play")
        print("2. Quit to Menu")
        choice = int(input("Choose any option to continue: "))
        clear_screen()
        if choice == 1:
            print("Running...")
        else:
            save_player_data("data/player.txt")
            print("Quitting to main menu...")
            to_run = False
        print("")


def show_options():  # Runs the options menu
    print("Options Menu!")
    print("")
    to_run = True
    while to_run:
        print("1. Browse options")
        print("2. Quit to Menu")
        choice = int(input("Choose any option to continue: "))
        clear_screen()
        if choice == 1:
            print("Browsing...")
        else:
            print("Quitting to main menu...")
            to_run = False
        print("")


def run_game():  # Runs the main menu window
    to_run = True
    while to_run:
        show_main_menu()
        choice = int(input("Choose any option to continue: "))
        clear_screen()
        if choice == 1:
            show_game()
        elif choice == 2:
            show_options()
        else:
            print("Game Ended!")
            to_run = False


def initialize(title):  # Starts the game
    clear_screen()
    show_title(title)
    run_game()
