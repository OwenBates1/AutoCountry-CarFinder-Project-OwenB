#VehiclesList
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


#MENU
def user_menu():
  print("*******************************\n"
     "AutoCountry Vehicle Finder v0.1\n"
      "*******************************\n")
  
#Display menu with options

user_menu()
userChoice = input("Please Enter the following number below from the following menu:\n"
                    "\n"  "1. PRINT all Authorized Vehicles"
                    "\n" "2. SEARCH for Authorized Vehicle"
                    "\n" "3. Exit ")


def full_menu():
  print("*******************************\n"
     "AutoCountry Vehicle Finder v0.1\n"
      "*******************************\n")
  input("Please Enter the following number below from the following menu:\n"
    "\n"  "1. PRINT all Authorized Vehicles"
    "\n" "2. SEARCH for Authorized Vehicle"
    "\n" "3. Exit ")



if userChoice == "1":
  for vehicle in AllowedVehiclesList:
    print(vehicle)
elif userChoice == "2":
  x = input("PLEASE ENTER THE FULL VEHICLE NAME: ")
  if x in AllowedVehiclesList:
      print(x + " is an authorized vehicle")
  else: 
      print( x + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
  full_menu()
elif userChoice == "3":
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
else:
  print("Invalid entry please try again")

