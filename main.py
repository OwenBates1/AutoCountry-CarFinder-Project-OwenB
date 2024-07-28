#VehiclesList
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


#MENU
def user_menu():
  print("*******************************\n"
     "AutoCountry Vehicle Finder v0.1\n"
      "*******************************\n")
  
#Display menu with options
def full_menu():
    user_menu()
    userChoice = input("Please Enter the following number below from the following menu:\n"
      "1. PRINT all Authorized Vehicles\n"
      "2. SEARCH for Authorized Vehicle\n"
      "3. ADD Authroized Vehicle\n"
      "4. Exit\n"
      "Choice: ")
    
    return userChoice
  

while True:
  userChoice = full_menu()

  if userChoice == "1":
    for vehicle in AllowedVehiclesList:
        print(vehicle)
  elif userChoice == "2":
    x = input("PLEASE ENTER THE FULL VEHICLE NAME: ")
    if x in AllowedVehiclesList:
        print(x + " is an authorized vehicle")
    else:
        print(x + " is not an authorized vehicle. Please check the spelling and try again.")
  elif userChoice == "3" :
    newVehicle = input("Please Enter the full Vehicle name you would like to add: ")
    AllowedVehiclesList.append(newVehicle) 
    print("You have added " + newVehicle + " as an authorized vehicle")
    
  
  elif userChoice == "4":
    print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
    break
  else:
    print("Invalid entry. Please try again.")
