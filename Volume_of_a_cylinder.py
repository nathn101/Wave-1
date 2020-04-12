import math
#Obtaining user inputs of radius and height
r = int(input("Enter a radius: "))
h = int(input("Enter a height: "))

#Calculating the volume of the cylinder
volume = (3.14 * r**2) * h

#Rounding the total volume to a total of one decimal place
round(volume, 1)

#Converting the volume to a string for compatibility with concatenation
volume = str(volume)

#Printing the results
print("The volume of the cylinder is " + volume + " units cubed")