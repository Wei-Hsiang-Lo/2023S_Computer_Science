import random
import turtle
from world import *
from plant import *
from lifeform import *

class Fish(LifeForm):
    def __init__(self):
        super().__init__()
        self.__starveTick = 0
        self.changeShape("fish.gif")

    def liveAlittle(self):
        offsetList = [(-1,1),  (0,1),  (1,1),
                       (-1,0),          (1,0),
                       (-1,-1), (0,-1), (1,-1)]
        adjFish = 0
        for offset in offsetList:
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            
            if 0 <= newX < self._LifeForm__world.getMaxX() and \
               0 <= newY < self._LifeForm__world.getMaxY():
                if (not self._LifeForm__world.emptyLocation(newX, newY)) and \
                   isinstance(self._LifeForm__world.lookAtLocation(newX, newY), Fish):
                    adjFish += 1
        
        if adjFish >= 2:
            self._LifeForm__world.delThing(self)
        else:
            self._LifeForm__breedTick += 1
            if self._LifeForm__breedTick >= 12:
                self.tryToBreed(Fish())	#try to breed
        self.tryToEat()
        if self.__starveTick == 5:
            print('***** one fish is dead *****')
            self._LifeForm__world.delThing(self)
        else:
            self.tryToMove()
    
    def tryToEat(self):
        #add the position of nearby plant to a list
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0),         (1, 0),
                      (-1, -1), (0, -1), (1, -1)]
        adjPrey = []
        for offset in offsetList:
            newX = self._LifeForm__xPos + offset[0]
            newY = self._LifeForm__yPos + offset[1]
            if 0 <= newX < self._LifeForm__world.getMaxX() and \
                0 <= newY < self._LifeForm__world.getMaxY():
                    if(not self._LifeForm__world.emptyLocation(newX, newY)) and \
                        isinstance(self._LifeForm__world.lookAtLocation(newX, newY), Plant):
                            adjPrey.append(self._LifeForm__world.lookAtLocation(newX, newY))
        #if there exists plant, randomly pick one plant in the list, and eat
        if len(adjPrey) > 0:
            prey = adjPrey[random.randrange(len(adjPrey))]
            preyX = prey.getX()
            preyY = prey.getY()
            self._LifeForm__world.delThing(prey)
            self.move(preyX, preyY)
            self.__starveTick = 0
        else:
            self.__starveTick += 1