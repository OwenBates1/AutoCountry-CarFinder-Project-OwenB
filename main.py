
#MENU
def user_menu():
  print("*******************************\n"
     "AutoCountry Vehicle Finder v0.4\n"
      "*******************************\n")
  
#Display menu with options
def full_menu():
    user_menu()
    userChoice = input("Please Enter the following number below from the following menu:\n"5
      "1. PRINT all Authorized Vehicles\n"
      "2. SEARCH for Authorized Vehicle\n"
      "3. ADD Authrorized Vehicle\n"
      "4. DELETE Authrorized Vehicle\n"
      "5. Exit\n"
      "Choice: ")
    
    return userChoice
  

while True:
  
  userChoice = full_menu()

  if userChoice == "1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    db = open("Vehicle.txt", "r")
    print(db.read())
  elif userChoice == "2":
    x = input("PLEASE ENTER THE FULL VEHICLE NAME: ")
    db = open("Vehicle.txt", "r")
    if x in db.read():
        print(x + " is an authorized vehicle")
    else:
        print(x + " is not an authorized vehicle. Please check the spelling"
              " and try again.")
  elif userChoice == "3" :
    newVehicle = input("Please Enter the full Vehicle name you would like to add: ")
    db = open("Vehicle.txt", "a")
    db.write(newVehicle + "\n")
    print("You have added " + newVehicle + " as an authorized vehicle")
  elif userChoice == "4":
    removeVehicle = input("Please Enter the full Vehicle name" 
                          " you would like to REMOVE: ")
    confirmed = input("Are you sure you want to remove " + removeVehicle + 
                      " from the Authorized Vehicle List? ")
    if confirmed == "yes":
      db = open("Vehicle.txt", "r")
      lines = db.readlines()
      db = open("Vehicle.txt", "w")
      for line in lines:
        if line.strip("\n") != removeVehicle:
          db.write(line)
          
    
      
       
    if confirmed == "no" "No":
          continue
  elif userChoice == "5":
    print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
    break
  else:
    print("Invalid entry. Please try again.")
