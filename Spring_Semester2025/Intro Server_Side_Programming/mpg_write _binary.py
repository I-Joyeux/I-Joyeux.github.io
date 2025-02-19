# Feb/15/2024
#!/usr/bin/env python3
import csv
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():

    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        more = input("More entries? (y or n): ")

            #   two -demensional list
        trips = []
        trips = [miles_driven, gallons_used, mpg]
        trips.append(trips)

        # save to trip.csv
        with open("trips.csv","w", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(trips)
        
    
    print("Bye!")

if __name__ == "__main__":
    main()

