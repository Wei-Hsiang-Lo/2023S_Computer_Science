import random
import turtle
from world import *

#this is the parent class of classes Plant, Fish, Bear
class LifeForm:
    def __init__(self):
        self.__xPos = 0
        self.__yPos = 0
        self.__world = None
        self.__breedTick = 0
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
    
    def getX(self):
        return self.__xPos
    
    def getY(self):
        return self.__yPos
    
    def setX(self, newX):
        self.__xPos = newX
    
    def setY(self, newY):
        self.__yPos = newY
    
    def setWorld(self, aWorld):
        self.__world = aWorld
    
    def appear(self):
        self.__turtle.goto(self.__xPos,self.__yPos)
        self.__turtle.showturtle()
    
    def hide(self):
        self.__turtle.hideturtle()
    
    def move(self, newX, newY):
        self.__world.moveThing(self.__xPos, self.__yPos, newX, newY)
        self.__xPos = newX
        self.__yPos = newY
        self.__turtle.goto(self.__xPos, self.__yPos)
    
    def tryToBreed(self, childThing):
        offsetList =  [(-1,1),  (0,1),  (1,1),
                       (-1,0),          (1,0),
                       (-1,-1), (0,-1), (1,-1)]
        i = random.randrange(len(offsetList))
        offset = offsetList[i]
        nextX = self.__xPos + offset[0]
        nextY = self.__yPos + offset[1]
        #choose a position randomly, if the position is in the grid. If the positon is illegal, generates a new position.
        while not ( 0 <= nextX < self.__world.getMaxX() and \
            0 <= nextY < self.__world.getMaxY() ):
            i = random.randrange(len(offsetList))
            offset = offsetList[i]
            nextX = self.__xPos + offset[0]
            nextY = self.__yPos + offset[1]        
        #if the new position is empty, generates a new obj and reset the breed time.
        if self.__world.emptyLocation(nextX, nextY):
            aNewThing = childThing
            self.__world.addThing(aNewThing, nextX, nextY)
            self.__breedTick = 0  #reset breedTick

    def tryToMove(self):
        offsetList =  [(-1,1),  (0,1),  (1,1),
                       (-1,0),          (1,0),
                       (-1,-1), (0,-1), (1,-1)]
        i = random.randrange(len(offsetList))
        offset = offsetList[i]
        nextX = self.__xPos + offset[0]
        nextY = self.__yPos + offset[1]
        #while the position is illegal, generates a new position.
        while not ( 0 <= nextX < self.__world.getMaxX() and \
            0 <= nextY < self.__world.getMaxY() ):
            i = random.randrange(len(offsetList))
            offset = offsetList[i]
            nextX = self.__xPos + offset[0]
            nextY = self.__yPos + offset[1]        
        #if the position is empty, move the obj to the new position.
        if self.__world.emptyLocation(nextX, nextY):
            self.move(nextX, nextY)
    
    def changeShape(self, newShape):
        self.__turtle.shape(newShape)