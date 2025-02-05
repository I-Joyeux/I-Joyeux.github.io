# Joyeux Irashubije
# 01/25/2025
#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)
Total_cost=cost*gallons_used
per_mile= Total_cost/miles_driven  #cost per mile is the total cost divided the miles driven
mpg = round(mpg, 1)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Gas cost:\t\t\t{Total_cost}")
print(f"cost per mile:\t\t\t{per_mile}")
print()
print("Bye!")


