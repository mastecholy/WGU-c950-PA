import csv
import datetime
import PackageData


# instantiation of the lists that will hold the distance table information
distanceData = []
addressData = []


# functions to parse the csv files and store the information into the above lists
def loadDistanceData(fileName):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for distances in csv_reader:
            distanceData.append(distances)


def loadAddressData(fileName):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for addresses in csv_reader:
            addressData.append(addresses[0])


loadAddressData('DistanceTable.csv')
loadDistanceData('DistanceTable.csv')


###################################################


# takes two address strings as input and gets their distance from the table info that was parsed into distanceData
def getDistance(address1, address2):
    addIndex1 = addressData.index(address1)
    addIndex2 = addressData.index(address2)
    if distanceData[addIndex1][addIndex2 + 1] != '':
        return float(distanceData[addIndex1][addIndex2 + 1])
    else:
        return float(distanceData[addIndex2][addIndex1 + 1])


# nearest neighbor greedy algorithm that returns the nearest address to fromAddress and the name of the address, O(n)
def minDistanceFrom(fromAddress, addressList):
    dist = 999
    tempAddress = None
    for address in addressList:
        if getDistance(fromAddress, address) < dist:
            dist = getDistance(fromAddress, address)
            tempAddress = address
    return dist, tempAddress


####################################################

# creation of the truck object, with individual start times and list of packages as parameters to manually load trucks
class Truck:
    def __init__(self, truckID, truckStartTime, packageList = []):
        self.id = truckID
        self.packageList = packageList
        self.startTime = truckStartTime
        self.distTraveled = 0

        for pkg in self.packageList:
            PackageData.packageTable.search(pkg).startTime = truckStartTime





#############################################################


# main self-adjusting algorithm, loops through all packages stored on truck, finds the time and distance of the nearest
# delivery location and removes that location from the list and updates the corresponding packages, does not need to
# loop through package locations, O(n^2)
def deliverPackages(truck):
    location = 'HUB'
    currentTime = truck.startTime
    addresses = []

    for pkg in truck.packageList:
        addresses.append(PackageData.packageTable.search(pkg).address)

    for package in truck.packageList:
        pkgOBJ = (PackageData.packageTable.search(package))
        tempDistance, tempAddress = minDistanceFrom(location, addresses)
        truck.distTraveled += tempDistance
        currentTime += datetime.timedelta(hours=tempDistance/18)
        pkgOBJ.status = 'delivered at {}'.format(currentTime)
        pkgOBJ.deliveryTime = currentTime
        addresses.remove(tempAddress)
        location = tempAddress

    returnDist = float(getDistance(location, 'HUB'))
    truck.distTraveled += returnDist
    currentTime += datetime.timedelta(hours=returnDist/ 18)
    return currentTime







