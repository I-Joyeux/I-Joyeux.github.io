# !/user/bin/env python3
# Joyeux Irashubije 04/03/2025

# display a welcome message
print("==================================================================")
print("               Baseball Team Manager")
print("This program calculates the batting average for a player based  on the player's official number of at bats and hits.")
print("==================================================================")
print()
print()

# User inputs
Player_Name=input("Player's name: ")
At_Bats=int(input("Official number of at bats: "))
Hits=int(input("Number of hits: "))

# Calculation  batting average 
Average = Hits / At_Bats
# displaying average
print(f"Pat's batting average is: {Average:.3f}")