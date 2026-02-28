#I write this program by myself Sign here:羅瑋翔
#Email address: xianglo9121.mg10@nycu.edu.tw
#Anything specail? I use different color to point out the point, the line in the graph and thoroughly check
#the two list are parallel, rather than follow the format of the csv file to write
#I provide addtional functions: (1)回歸直線 (2)correlation funciton
import turtle
import csv
import statistics

def calCorrelation(list_1, list_2, mean_1, mean_2,stdev_1, stdev_2):
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.setworldcoordinates(min(list_1)-20, min(list_2)-20, max(list_1)+20, max(list_2)+20)

    #draw the y axis and x axis
    t.up()
    t.goto(min(list_1)-10,min(list_2)-10)
    t.down()
    t.goto(min(list_1)-10, max(list_2)+10)
    t.up()
    t.goto(min(list_1)-10,min(list_2)-10)
    t.down()
    t.goto(max(list_1)+10, min(list_2)-10)
    t.up()

    numer = 0
    deno = 0
    for i in range(len(list_1)):
        #draw the point
        t.color('blue')
        t.goto(list_1[i], list_2[i])
        t.dot()
        t.speed(10)
        #calculate the sum of the numerator
        numer = (list_1[i] - mean_1)*(list_2[i] - mean_2) + numer
        deno = deno + (list_1[i] - mean_1)**2
    
    r = numer / ((len(list_1) - 1) * stdev_1 * stdev_2)
    b = numer / deno
    t.color('black')
    t.up()
    t.goto(min(list_1) + 20, min(list_2) - 20)
    t.down()
    t.write('r = {}'.format(r), font = ("Helvetica", 16, "bold"))
    #畫出回歸直線
    t.up()
    t.color('RED')
    t.goto(min(list_1), mean_2 - b*mean_1 + b * min(list_1))
    t.down()
    t.goto(max(list_1), mean_2 - b*mean_1 + b * max(list_1))
    t.up()
    t.goto(min(list_1) + 40, min(list_2) + 10)
    t.write('y = {0:.4f}x + {1:.4f}'.format(b, mean_2 - b * mean_1), font = ("Helvetica", 16, "bold"))
    
    wn.exitonclick()
    
with open('DIS.csv','r',encoding='cp1252') as inFileDis:
    with open('META.csv','r',encoding='cp1252') as inFileMeta:
        
        theReaderDis = csv.reader(inFileDis)
        theTitleDis = next(theReaderDis)
        theReaderMeta = csv.reader(inFileMeta)
        theTitleMeta = next(theReaderMeta)

        #find date column in the table
        colDate_1 = 0
        colDate_2 = 0
        while theTitleDis[colDate_1] != 'Date':
            colDate_1 += 1
        while theTitleDis[colDate_2] != 'Date':
            colDate_2 += 1
            
        #find closing column in the table
        colClosing_1 = 0
        colClosing_2 = 0
        while theTitleDis[colClosing_1] != 'Close':
            colClosing_1 += 1
        while theTitleDis[colClosing_2] != 'Close':
            colClosing_2 += 1
        
        #construct a date and a closing data for DIS and META
        dateListDis = []
        dateListMeta = []
        oldCloDisList = []
        oldCloMetaList = []
        for aLine in theReaderDis:
            dateListDis.append(aLine[colDate_1])
            oldCloDisList.append(float(aLine[colClosing_1]))
        for aLine in theReaderMeta:
            dateListMeta.append(aLine[colDate_2])
            oldCloMetaList.append(float(aLine[colClosing_2]))

        #ensure that the length of the lists are the same and make them parallel
        cloDisList = []
        cloMetaList = []
        for i in range(len(dateListDis)):
            for j in range(len(dateListMeta)):
                if dateListDis[i] == dateListMeta[j]:
                    cloDisList.append(oldCloDisList[i])
                    cloMetaList.append(oldCloMetaList[j])
        
        DisMean = statistics.mean(cloDisList)
        MetaMean = statistics.mean(cloMetaList)
        DisStdev = statistics.stdev(cloDisList)
        MetaStdev = statistics.stdev(cloMetaList)
        
        #call the function to draw the correlation graph and calculate r
        calCorrelation(cloDisList, cloMetaList, DisMean, MetaMean, DisStdev, MetaStdev)
