import random
import turtle

class World:
    def __init__(self, mX, mY):
        self.__maxX = mX
        self.__maxY = mY
        self.__thingList = []
        
        self.__grid = []
        for aRow in range(self.__maxY):
            row = [None for aCol in range(self.__maxX)]
            self.__grid.append(row)
        
        self.__wScreen = turtle.Screen()
        self.__wScreen.setworldcoordinates(-1, -1, self.__maxX, self.__maxY)
        #add three gif file, to present bear, fish, plant, respectively
        self.__wScreen.addshape("bear.gif")
        self.__wScreen.addshape("fish.gif")
        self.__wScreen.addshape("seaweed.gif")
        
        self.__wTurtle = turtle.Turtle()
        self.__wTurtle.hideturtle()

    def draw(self):
        self.__wScreen.tracer(0)
        self.__wTurtle.color("silver")
        
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        
        #draw horizontal lines
        self.__wTurtle.left(180)
        for i in range(self.__maxY - 2):
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
            self.__wTurtle.forward(self.__maxX - 1)
            self.__wTurtle.backward(self.__maxX - 1)
            self.__wTurtle.left(90)
        
        #draw vertical lines
        self.__wTurtle.right(180)
        self.__wTurtle.forward(self.__maxY - 2)
        self.__wTurtle.left(90)
        for i in range(self.__maxX - 2):
            self.__wTurtle.forward(1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(self.__maxY - 1)
            self.__wTurtle.backward(self.__maxY - 1)
            self.__wTurtle.right(90)
        
        self.__wTurtle.backward(self.__maxX - 2)
        self.__wScreen.tracer(1)

    #add aThing on the position (x, y) in the world
    def addThing(self, aThing, x, y): 
        #operations for aThing
        aThing.setX(x)
        aThing.setY(y)
        aThing.setWorld(self)
        aThing.appear()
        #operations for self
        self.__grid[y][x] = aThing
        self.__thingList.append(aThing)
    
    #delete athing in the world
    def delThing(self, aThing):
        #operations for aThing
        aThing.hide()
        #operations for self
        self.__grid[aThing.getY()][aThing.getX()] = None
        self.__thingList.remove(aThing)
    
    #move athing
    def moveThing(self, oldX, oldY, newX, newY):
        self.__grid[newY][newX] = self.__grid[oldY][oldX]
        self.__grid[oldY][oldX] = None
    
    def getMaxX(self):
        return self.__maxX
    
    def getMaxY(self):
        return self.__maxY
    
    #randomly choose a thing and execute the function liveAlittle()
    def liveALittle(self):
        if self.__thingList != []:
            i = random.randrange(len(self.__thingList))
            theThing = self.__thingList[i]
            theThing.liveAlittle()
    
    #check if the input position (x, y) is empty
    def emptyLocation(self, x, y):
        if self.__grid[y][x] == None:
            return True
        else:
            return False
    
    #to see what thing is on the position (x, y) (bear/fish/plant/none)
    def lookAtLocation(self, x, y):
        return self.__grid[y][x]
    
    #freeze the window
    def freezeWorld(self):
        self.__wScreen.exitonclick()