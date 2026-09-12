print("Select your ride: ")
print ("1. Bike")
print("2. Car")

#take input of number 1 or 2
#select your ride
choice = int( input("Enter your choice: ") )

#User entering option 1
if( choice== 1 ): #condition 1 outer if statement
    print("what type of bike")
    print ("1.Scooty\n")
    print ("2.Scooter\n")

    choice2=int(input("enter you choice 2: "))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")

elif ( choice ==2):
    print("what type of car do you choose")
    print("1.sedan")
    print("2.SUV")
    choice3=int(input("enter your choice3: "))

    if choice3==1:

        print("you have selected sedan")
    else:
        print("you have selected SUV")

else:
    print("Wrong choice!")
