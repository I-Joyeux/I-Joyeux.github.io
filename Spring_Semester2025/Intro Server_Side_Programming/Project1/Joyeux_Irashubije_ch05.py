# !/user/bin/env python3
# Joyeux Irashubije 04/03/2025

# display a welcome message
def Separator_Line():
    print("=============================================")
def Title():
    print("            Baseball Team Manager")
def Menu_Options():
    print("MENU options")
    print("1 – Calculate batting average ")
    print("2 - Exit program  ")
def Calculate_Average(Hits,At_Bats):
     # Calculation  batting average and displaying it
    Average = Hits / At_Bats
    return Average

# User inputs
Menu_Options()
def main():
    Separator_Line()
    Title()
    Menu_Options()
    Separator_Line()
    Menu_Option=input("MENU options: ") 
    while True:
        if Menu_Option == "1":
            print("Calculate batting average... ")
            # Player_Name = input("Player's name: ")
            At_Bats = int(input("Official number of at bats: "))
            Hits = int(input("Number of hits: "))

            # Calculation  batting average and displaying it
            Average= Calculate_Average(At_Bats,Hits)
            print(f" Batting average : {Average:.3f}")

            Menu_Option = input("MENU options: ")  # Ask for input again to continue or break

        elif Menu_Option == "2":
            break

        else:
            print("MENU options are only 1 and 2, try again")
            print
            Menu_Option = input("MENU options: ")
    print("Bye!")        
if __name__ == "__main__":
    main()  