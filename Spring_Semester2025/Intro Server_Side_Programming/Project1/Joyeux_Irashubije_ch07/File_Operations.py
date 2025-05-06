#!/user/bin/env python3
# Joyeux Irashubije 04/11/2025

# display a welcome message
import csv

# something went wrong 
def read_player_data(filename="lineup.csv"):
    players = []  # Initialize an empty list to store player data
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    name, position, at_bats_str, hits_str, average_str = row
                    at_bats = int(at_bats_str)
                    hits = int(hits_str)
                    average = float(average_str)
                    #A single player's data.
                    player_data = [name, position, at_bats, hits, average]
                    # Add the player's data to the 'players' list.
                    players.append(player_data)
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist yet
    except Exception as e:
        print(f"something went wrong reading player data from '{filename}': {e}")
        players = [] # ensure we return an empty list
    return players

# Writes player data to a CSV file, Name,Position,At_Bats,Hits,Average
def write_player_data(players, filename="lineup.csv"): #writting to a file named lineup.csv
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(players)

    # Handle any exceptions that might occur during file writing.
    except Exception as e:
        print(f"something went wrong when writing player data to '{filename}': {e}")