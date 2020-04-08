#Obtaining user input assuming every input is a number
w = float(input("Enter a width: "))
l = float(input("Enter a length: "))

#Conversion to acres
a = (w * l) / 43560

#Conversion back to string for concatenation
a = str(a)
#Print amount of acres
print("The area of the field in acres is: " + a + " square acres")