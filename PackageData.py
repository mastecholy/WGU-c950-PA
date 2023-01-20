import csv
import datetime


# Hash table object that will be used for the table of packages is created first with exact capacity for num of packages
class HashTable:

    def __init__(self, initialCapacity=40):
        self.table = []
        for i in range(initialCapacity):
            self.table.append([])

# The function that inserts the package to a unique bucket with the package ID being the key, O(n)
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]
        bucketList.append(item)

        for kv in bucketList:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucketList.append(key_value)
        return True

# 1-1 search function that returns the resulting item in the bucket for its key, O(1)
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]

        for key_value in bucketList:
            if key_value[0] == key:
                return key_value[1]
        return None


# Remove function operating similar to the search function but removing instead of returning, O(1)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]

        for kv in bucketList:
            if kv[0] == key:
                bucketList.remove([kv[0], kv[1]])


# Package class with parameters to store all necessary package information
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status

    def __getitem__(self, i):
        return f"Value {i}"

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.mass, self.notes, self.status)

# Derive the status based on the delivery time, truck start time, user requested time, with specific stipulations
# for package 9, project specific, O(n)
    def getStatusForTime(self, requestedTime):
        package_status = 'at hub'

        if self.id == 9:
            self.address = '300 State St'
        if requestedTime > self.deliveryTime:
            if self.id == 9:
                self.address = '410 S State St'
            package_status = 'delivered at {}'.format(self.deliveryTime)
        elif self.startTime < requestedTime < self.deliveryTime:
            if self.id == 9:
                self.address = '410 S State St'
            package_status = 'en route'
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.mass, self.notes, package_status)


# Parses information from csv file, turns line into package object and inserts it into package hash table O(n)
def loadPackageData(fileName):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for package in csv_reader:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pNotes = package[7]
            pStatus = "at hub"

            package = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus)

            packageTable.insert(pID, package)


# Searches through the hash table for a specific address to return the IDs of any packages with the address, O(n)
def getAddressIDs(address):
    idList = []
    for id in range(40):
        if packageTable.search(id+1).address == address:
            idList.append(id+1)
    return idList


# creation and loading of the package hash table
packageTable = HashTable()
loadPackageData('PackageFile.csv')

