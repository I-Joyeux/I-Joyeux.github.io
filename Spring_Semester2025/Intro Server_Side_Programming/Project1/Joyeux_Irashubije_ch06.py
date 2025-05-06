#!/user/bin/env python3
# Joyeux Irashubije 04/11/2025

# display a welcome message
def Separator_Line():
    print("=============================================")

def Title():
    print("                    Baseball Team Manager")

def Menu_Options():
    print("MENU options")
    print("1 – Display lineup ")
    print("2 – Add player ")
    print("3 – Remove player ")
    print("4 – Move player ")
    print("5 – Edit player position")
    print("6 – Edit player stats ")
    print("7 - Exit program ")
    print()
    print("Position")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

def Calculate_Average(Hits, At_Bats):
    # Calculation  batting average and displaying it
    Average = int(Hits) / int(At_Bats)
    return f"{Average:.3f}" # Format to 3 decimal places

def Display(Players):
    if len(Players) == 0:
        print("There are no Players in the database/list.\n")
        return
    else:
        print("LINEUP:")
        for i, Player in enumerate(Players, start=1):
            print(f"{i}. {Player[0]} ({Player[1]})  AB: {Player[2]}, H: {Player[3]}, AVG: {Player[4]}")
        print()

def Add(Players, valid_positions):
    Name = input("Name: ")
    while True:
        Position = input("Position: ").upper() # Convert to uppercase for case-insensitive comparison
        if Position in valid_positions:
            break
        else:
            print(f"Invalid position. Valid positions are: {', '.join(valid_positions)}")

    while True:
        At_Bats_str = input("At Bats: ")
        if At_Bats_str.isdigit():
            At_Bats = int(At_Bats_str)
            break
        else:
            print("Invalid input. At Bats must be a number.")

    while True:
        Hits_str = input("Hits: ")
        if Hits_str.isdigit():
            Hits = int(Hits_str)
            break
        else:
            print("Invalid input. Hits must be a number.")

    Average = Calculate_Average(Hits, At_Bats)
    Player = [Name, Position, At_Bats, Hits, Average]
    Players.append(Player)
    print(f"{Name} was added as a {Position}.\n")

def Delete(Players):
    if not Players:
        print("There is no players to remove,sorry.\n")
        return
    # chech if an int is entered and that it falls in the rage
    while True:
        number_str = input("Enter the number of the player to remove: ")
        if number_str.isdigit():
            number = int(number_str)
            if 1 <= number <= len(Players):
                Player = Players.pop(number-1)
                print(f"{Player[0]} was deleted.\n")
                break
            else:
                print("Invalid player number.\n")
        else:
            print("Invalid input. Please enter a number.\n")

def Move_Player(Players):
    if len(Players) < 2:
        print("Not enough players to move.\n")
        return
    Display(Players)
    while True:
        from_num_str = input("Current lineup number: ")
        if from_num_str.isdigit():

            from_num = int(from_num_str)
            if 1 <= from_num <= len(Players):
                print(f"Player at lineup number {from_num}: {Players[from_num - 1]}")
                break
            else:
                print("Invalid player number.\n")
        else:
            print("Invalid input. Please enter a number.\n")

    while True:
        to_num_str = input("E new lineup number : ")
        if to_num_str.isdigit():
            to_num = int(to_num_str)
            if 1 <= to_num <= len(Players):
                player_to_move = Players.pop(from_num - 1)
                Players.insert(to_num - 1, player_to_move)
                print(f"{player_to_move[0]} was moved to position {to_num}.\n")
                break
            else:
                print("Invalid position number.\n")
        else:
            print("Invalid input. Please enter a number.\n")

def Edit_Position(Players, valid_positions):
    if not Players:
        print("There are no players to edit.\n")
        return
    Display(Players)
    player_index_str = input("Enter the number of the player to edit position: ")
    if player_index_str.isdigit():
        player_index = int(player_index_str) - 1
        if 0 <= player_index < len(Players):
            player_name = Players[player_index][0]
            while True:
                new_position = input(f"Enter the new position for {player_name}: ").upper()
                if new_position in valid_positions:
                    Players[player_index][1] = new_position
                    print(f"{player_name}'s position updated to {new_position}.\n")
                    break
                else:
                    print(f"Invalid position: {new_position}. Valid positions are: {', '.join(valid_positions)}")
        else:
            print("Invalid player number.\n")
    else:
        print("Invalid input. Please enter a number.\n")

def Edit_Stats(Players):
    if not Players:
        print("There are no players to edit stats for.\n")
        return
    Display(Players)
    player_index_str = input("Enter the number of the player to edit stats: ")
    if player_index_str.isdigit():
        player_index = int(player_index_str) - 1
        if 0 <= player_index < len(Players):
            player_name = Players[player_index][0]
            while True:
                at_bats_str = input(f"Enter the new At Bats for {player_name}: ")
                if at_bats_str.isdigit():
                    Players[player_index][2] = int(at_bats_str)
                    break
                else:
                    print("try again. At Bats must be a number.")
            while True:
                hits_str = input(f"Enter the new Hits for {player_name}: ")
                if hits_str.isdigit():
                    Players[player_index][3] = int(hits_str)
                    break
                else:
                    print("try again. Hits must be a number.")
            Players[player_index][4] = Calculate_Average(Players[player_index][3], Players[player_index][2])
            print(f"Stats updated for {player_name}.\n")
        else:
            print("Invalid player number.\n")
    else:
        print("Invalid input. Please enter a number.\n")

def main():

    Players = []
    Positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


    Separator_Line()
    Title()
    Menu_Options()
    Separator_Line()

    while True:
        command = input("Enter a command (1-7): ")
        if command == "1":
            Display(Players)
        elif command == "2":
            Add(Players, Positions)
        elif command == "3":
            Delete(Players)
        elif command == "4":
            Move_Player(Players)
        elif command == "5":
            Edit_Position(Players, Positions)
        elif command == "6":
            Edit_Stats(Players)
        elif command == "7":
            print("Exiting program. Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()