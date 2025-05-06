# !/user/bin/env python3
# Joyeux Irashubije 04/03/2025

# display a welcome message
print("=============================================")
print("            Baseball Team Manager")
print("MENU options")
print("1 – Calculate batting average ")
print("2 - Exit program  ")
print("=============================================")

# User inputs
Menu_Option = input("MENU options: ")
while True:
    if Menu_Option == "1":
        print("Calculate batting average... ")
        Player_Name = input("Player's name: ")
        At_Bats = int(input("Official number of at bats: "))
        Hits = int(input("Number of hits: "))

        # Calculation  batting average and displaying it
        Average = Hits / At_Bats
        print(f"{Player_Name}'s batting average is: {Average:.3f}")
        print()

        Menu_Option = input("MENU options: ")  # Ask for input again to continue or break
    
    elif Menu_Option == "2":
        break

    else:
        print("MENU options are only 1 and 2, try again")
        print
        Menu_Option = input("MENU options: ")
print("Bye")        