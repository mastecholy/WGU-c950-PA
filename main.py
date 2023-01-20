#Massimiliano Petrizzi ID: 001386173

import datetime
import PackageData
import DeliveryData

# Function that loops the constant time search function to obtain a package object and trigger an object method
def getStatusAtTime(time):
    for i in range(1,41):
        print(PackageData.packageTable.search(i).getStatusForTime(time))


menuChoices = {
    1: 'Print all packages',
    2: 'Print package information at a specific time',
    3: 'Print total distance traveled by delivery trucks',
    4: 'Exit'
}


# Prints the menu options stored above in a dictionary to the user interface
def printMenu():
    for key in menuChoices.keys():
        print(key, '--', menuChoices[key])


# This chain of code calls all the necessary functions for the entire loading and delivery process
# The trucks are manually loaded with their packages and their start time is set
truck1 = DeliveryData.Truck(1, datetime.timedelta(hours=8), [13, 14, 15, 16, 19, 20, 29, 1, 30, 31, 40, 37, 34])

truck2 = DeliveryData.Truck(2, datetime.timedelta(hours=9, minutes=5), [18, 36, 3, 38, 6, 25, 5, 24, 23, 26, 10, 22])

# The trucks then deliver their packages in order, and return to the hub while tallying their mileage
DeliveryData.deliverPackages(truck1)

totalDistanceTraveled = truck1.distTraveled

truck1 = DeliveryData.Truck(1, datetime.timedelta(hours=10, minutes=20), [9, 28, 32, 27, 35, 7, 19, 39, 2, 33, 11, 8, 17, 12, 21, 4])

PackageData.packageTable.search(9).address = '410 S State St'

DeliveryData.deliverPackages(truck1)

totalDistanceTraveled += truck1.distTraveled

DeliveryData.deliverPackages(truck2)

totalDistanceTraveled += truck2.distTraveled


print('\n\nWelcome to the WGUPS Package Routing Program\n')

# Constant loop that outputs options for the user and prints requested info or terminates the program
while True:
    printMenu()
    option = int(input('Enter your choice: '))

    if option == 1:
        print('\nAll package data: \n')
        for i in range(40):
            print(PackageData.packageTable.search(i+1))
        print('\n\n')

    elif option == 2:
        hour = int(input('Enter the hour: '))
        minute = int(input('Enter the minutes: '))
        time = datetime.timedelta(hours=hour, minutes=minute)
        print('\nAll package data at %s \n' % time)
        getStatusAtTime(time)
        print('\n\n')

    elif option == 3:
        print('\nTotal miles traveled by delivery trucks: %s\n\n' % totalDistanceTraveled)

    elif option == 4:
        break

    else:
        print('\nInvalid choice, please try again.\n\n')









