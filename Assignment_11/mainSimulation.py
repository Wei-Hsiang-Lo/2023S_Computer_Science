import random
import turtle
from world import *
from plant import *
from fish import *
from bear import *
from lifeform import *

def mainSimulation():
    #this part enables the users to input the initial circumstances of the imitating world
    numberOfBears = int(input("Enter the number of bear (non-negative integer): "))
    numberOfFish = int(input("Enter the number of fish (non-negative integer): "))
    numberOfPlants = int(input("Enter the number of plant (non-negative integer): "))
    worldLifeTime = int(input("Enter the Life time (non-negative integer): "))
    worldWidth = int(input("Enter the width of the world (non-negative integer): "))
    worldHeight = int(input("Enter the height of the world (non-negative integer): "))

    myWorld = World(worldWidth, worldHeight)
    myWorld.draw()

    #generating the plant/fish/bear randomly on the grid.
    for i in range(numberOfPlants):
        newPlant = Plant()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newPlant, x, y)

    for i in range(numberOfFish):
        newPlant = Fish()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newPlant, x, y)

    for i in range(numberOfBears):
        newPlant = Bear()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newPlant, x, y)

    for i in range(worldLifeTime):
        myWorld.liveALittle()
        print('current life time :', i)

    myWorld.freezeWorld()