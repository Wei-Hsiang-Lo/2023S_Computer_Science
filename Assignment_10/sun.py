import turtle

class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__x = 0
        self.__y = 0
        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.shape('circle')
        self.__sTurtle.color('yellow')

    def getName(self):
        return self.__name
    
    def getRadius(self):
        return self.__radius
    
    def getMass(self):
        return self.__mass
    
    def getTemp(self):
        return self.__temp
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
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
    
    def setName(self, newName):
        self.__name = newName

    def setRadius(self, newRadius):
        self.__radius = newRadius
    
    def setMass(self, newMass):
        self.__mass = newMass

    def setTemp(self, newTemp):
        self.__temp = newTemp

    def setX(self, newX):
        self.__x = newX
    
    def setY(self, newY):
        self.__y = newY

    def setShape(self, newShape):
        self.__shape = newShape

    def __str__(self):
        return self.__name 