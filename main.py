AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def menu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please Enter the following number below from the following menu:")
  print()
  print("1. PRINT all Authorized Vehicles")
  print("2. Search for Authorized Vehicles")
  print("3. ADD Authorized Vehicle")
  print("4. Exit")
  print("********************************\n")
  
def program():
  menu()
  menuChoice = input()

  if menuChoice == "1" or menuChoice == "2" or menuChoice == "3":
    if menuChoice == "1":
      print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n")
      for c in range(len(AllowedVehiclesList)):
        print(AllowedVehiclesList[c])
      program()
    if menuChoice == "2":
      searchChoice = input("\nPlease Enter the full Vehicle name: ")
      if searchChoice in AllowedVehiclesList:
        print (searchChoice, "is an authorized vehicle\n")
      else:
        print (searchChoice, "is not an authorized vehicle, if you received this in error please check the spelling and try again\n")
      program(AllowedVehiclesList) 
    if menuChoice == "3":
      addChoice = input("\nPlease Enter the full Vehicle name you would like to add:")
      AllowedVehiclesList.append(addChoice)
      print("\nYou have added " + addChoice + " as an authorized vehicle")
      program()
    if menuChoice == "4":
      quit("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
  else:
    print("\nInvalid choice\n")
    program()

program()