#VehiclesList
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


#MENU
print("*******************************\n"
     "AutoCountry Vehicle FInder v0.1\n"
      "*******************************\n")

userChoice = input("Please Enter the following number below from the following menu:\n"
                 "\n"  "1. PRINT all Authorized Vehicles"
                   "\n" "2. Exit ")

if userChoice == "1":
  for vehicles in AllowedVehiclesList:
    print(vehicles)
elif userChoice == "2":
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
else:
  print("Invalid entry please try again")