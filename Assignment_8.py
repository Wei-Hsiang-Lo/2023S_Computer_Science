#I write this program by myself. Sign here: 羅瑋翔
#Email address: xianglo9121.mg10@nycu.edu.tw
#Anything special? i comment a lot to help understand the code
#None
import csv
import random
import math

def readFile(filename, str):
    with open (filename, "r", encoding = 'utf-8') as inFile:
        #read the input file
        theReader = csv.reader(inFile)
        theTitle = next(theReader)

        #find the column of string, which could represent latitute and longitute
        col = 0
        while theTitle[col] != str:
            col = col + 1

        #create the Dictionary of latitute or longitute
        aList = []
        #add the elements to the dictionary
        for aLine in theReader:
            value = float(aLine[col])
            aList.append(value)
    return aList

def combine(latiList, longiList):
    dataDict = {}
    key = 0
    for i in range(len(latiList)):
        key = key + 1
        dataDict[key] = [latiList[i], longiList[i]]
    return dataDict

def createCentroids(k, dataDict):
    centroids = []
    selectedKeys = []
    count = 0
    while count < k:
        rKey = random.randint(1, len(dataDict))
        if rKey not in selectedKeys:
            selectedKeys.append(rKey)
            centroids.append(dataDict[rKey])
            count = count + 1
    return centroids

def eucliD(p1, p2):
    total = 0
    for i in range(len(p1)):
        diff = (p1[i] + p2[i]) ** 2
        total = total + diff
    eucliDistance = math.sqrt(total)
    return eucliDistance

def createClusters(k, centroids, dataDict, repeats):
    for aPass in range(repeats):
        print("*****", aPass + 1, "*****")
        clusters = [[] for i in range(k)]
        
        for key in dataDict:
            distances = []
            for i in range(k):
                d = eucliD(dataDict[key], centroids[i])
                distances.append(d)
            minD = min(distances)
            minI = distances.index(minD)
            clusters[minI].append(key)

        dimensions = len(dataDict[1])
        for i in range(k):
            sums = [0 for j in range(dimensions)]
            clusterLen = len(clusters[i])
            for key in clusters[i]:
                dataPoint = dataDict[key]
                for j in range(dimensions):
                    sums[j] = sums[j] + dataPoint[j]
            for j in range(dimensions):
                if clusterLen != 0:
                    sums[j] = sums[j] / clusterLen
            centroids[i] = sums

        for aCluster in clusters:
            print("CLUSTER", end = " ")
            for key in aCluster:
                print(dataDict[key], end = "")
            print()
    return clusters


print("The goal of this program is aimed to find the clusters of latitude and longitude")
repeats = int(input("Please enter how many times do you want to repeat on creating clusters (a positive integer): "))
k = int(input("Enter the numbers of clusters (a positive integer): "))
filename = input("Please enter the file name (an earthquake file in csv): ")

#code to output the dictionary
print('The dictionary : ')

#create k initial centroids
latitude = readFile(filename, 'latitude')
longitude = readFile(filename, 'longitude')
#combine the two list to a dictionary
dataDict = combine(latitude, longitude)
#find the centroids
centroids = createCentroids(k, dataDict)

print('The', k, 'initial centroids', end = " ")
for i in centroids:
    print(i, end = " ")
print()
createClusters(k, centroids, dataDict, repeats)