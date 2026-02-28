#I write this progam by myself. Sign here: 羅瑋翔
#Email Address: xianglo9121.mg10@nycu.edu.tw
#Anything Special? my program is a little differnt from the lecture notes
#in setworldcoordinate bar 
#I enable the users to input the list that thay want to turn it into bar chart
import turtle

def frequencyChart(aList):
    #construct a dictionary
    aDict = {}
    for item in aList:
        aDict[item] = aDict.get(item,0) + 1

    #sort-according to the keys in the dictionary
    itemList = list(aDict.keys())
    itemList.sort()

    #find the number of keys
    numKey = len(itemList)

    #find highest frequency
    valueList = list(aDict.values())
    highestFreq = max(valueList)

    wn = turtle.Screen()
    wn.setworldcoordinates(-1, -1, numKey, highestFreq + 1)
    t = turtle.Turtle()

    #draw vertical axis
    t.up()
    t.goto(-1, 0)
    t.down()
    t.write("0", font = ("Helvetica", 16, "bold"))
    t.up()
    t.goto(-1, highestFreq)
    t.down()
    t.write(highestFreq, font = ("Helvetica", 16, "bold"))

    #draw horizontal axis
    t.up()
    t.goto(0,0)
    t.down()
    t.goto(numKey-1, 0)

    #for each key, write the key and fraw its bar
    i = 0
    for item in itemList:
        t.up()
        t.goto(i, -1)
        t.down()
        t.write(item, font = ("Helvetica", 16, "bold"))
        t.up()
        t.goto(i, 0)
        t.down()
        t.goto(i, aDict[item])
        i = i + 1

    wn.exitonclick()
    
inString = input("Please enter the item and seperate each of them with a blank : ")
inList = inString.split()
inList = list(map(int, inList))
print("The list you entered is :", inList)
frequencyChart(inList)
