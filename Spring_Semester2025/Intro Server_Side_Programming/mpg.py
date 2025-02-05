# Joyeux Irashubije Feb/05/2025

#!/usr/bin/env python3
again="y"
# display a welcome message
print("The Miles Per Gallon program")
print()

while again.lower()=="y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost=float(input("Enter cost per gallon       "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    
    #calculating 
    mpg = round(miles_driven / gallons_used, 2) 
    Total=round(gallons_used*cost,2)
    cost_mile=round(Total/miles_driven,2)
    
    # display all the calculation
    print()
    print("Miles Per Gallon:          ", mpg)
    print("Total Gas cost:            ", Total)
    print("Cost per Mile:             ", cost_mile)
    
    print()
    again=input("Get entries for another trip (y/n)? ")
print()
print("Bye!")



