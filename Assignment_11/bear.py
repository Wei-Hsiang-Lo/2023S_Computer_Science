import random
import turtle
from world import *
from fish import *
from lifeform import *

class Bear(LifeForm):
    def __init__(self):
        super().__init__()
        self.__starveTick = 0
        self.changeShape("bear.gif")
    
    def liveAlittle(self):
        self._LifeForm__breedTick += 1
        if self._LifeForm__breedTick >= 8:
            self.tryToBreed(Bear())
        self.tryToEat()
        if self.__starveTick == 10:
            print('***** one bear is dead *****')
            self._LifeForm__world.delThing(self)
        else:
            self.tryToMove()

    def tryToEat(self):
        #add the position of nearby fish to a list
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
                        isinstance(self._LifeForm__world.lookAtLocation(newX, newY), Fish):
                            adjPrey.append(self._LifeForm__world.lookAtLocation(newX, newY))
        #if there exists fish, randomly pick one fish in the list, and eat.
        if len(adjPrey) > 0:
            prey = adjPrey[random.randrange(len(adjPrey))]
            preyX = prey.getX()
            preyY = prey.getY()
            self._LifeForm__world.delThing(prey)
            self.move(preyX, preyY)
            self.__starveTick = 0
        else:
            self.__starveTick += 1