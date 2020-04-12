#Obtaining the users input
PV = int(input("Enter deposit amount here: "))

#Used a for loop to reduce the number of variables created
for i in range (3):

    #Calculating the total balance
    Total = PV * (1 + 0.04)
    
    #Rounding the total to 2 decimal places
    Rounded_Total = str(round(Total,2))

    #Converting i to a string to be used for counting the year number
    i = str(i + 1)

    #Printing the results of the new balance
    print("Year " + i + ": $" + Rounded_Total)

    #Updating the new balance in the bank account
    PV = Total