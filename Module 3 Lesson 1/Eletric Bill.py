# Take input of number of units consumed from the usen
units = int(input(" Please enter Number of Units vou Consumed  : "))
# Check conditions of units consumed
# Then calculate amoun and surcharge accordingly.
# surcharge is the tax value


# Check for units less than 50
# Check for units less than 50
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# Check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

#Check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 75

else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %.2f" %total)
