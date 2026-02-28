import random
import turtle
from lifeform import *
from world import *

class Plant(LifeForm):
    def __init__(self):
        super().__init__()
        self.changeShape("seaweed.gif")

    def liveAlittle(self):
        self._LifeForm__breedTick += 1
        if self._LifeForm__breedTick >= 5:   #if the breedTick >= 5, generate a new plant
            self.tryToBreed(Plant())