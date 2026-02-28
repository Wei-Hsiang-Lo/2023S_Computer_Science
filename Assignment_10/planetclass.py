import turtle

class Planet:
    def __init__(self, iName, iRad, iM, iDist, iC, ishape, iVelX, iVelY):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVelX
        self.__velY = iVelY
        self.__x = self.__distance
        self.__y = 0
        self.__color = iC
        self.__pTurtle = turtle.Turtle()
        self.__shape = ishape
        self.__pTurtle.shape(self.__shape)
        self.__pTurtle.color(self.__color)
        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def getName(self):
        return self.__name
    
    def getRadius(self):
        return self.__radius
    
    def getMass(self):
        return self.__mass
        
    def getDistance(self):
        return self.__distance
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def getColor(self):
        return self.__color

    def getVolume(self):
        import math
        v = (4 / 3) * math.pi * self.__radius ** 3
        return v
    
    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius ** 2
        return sa
    
    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d
    
    def getVelX(self):
        return self.__velX
    
    def getVelY(self):
        return self.__velY
    
    def setName(self, newName):
        self.__name = newName

    def setRadius(self, newRadius):
        self.__radius = newRadius
    
    def setMass(self, newMass):
        self.__mass = newMass
    
    def setDistance(self, newDistance):
        self.__distance = newDistance

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY

    def setColor(self, newColor):
        self.__color = newColor

    def setShape(self, newShape):
        self.__shape = newShape

    def setVelX(self, newVelX):
        self.__velX = newVelX

    def setVelY(self, newVelY):
        self.__velY = newVelY

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def __str__(self):
        return self.__name