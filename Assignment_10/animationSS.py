from sun import *
from planetclass import *
from solarsystem import *

def createSSandAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("SUN", 500, 10, 5800)
    ss.addSun(sun)

    p = Planet("MERCURY", 19.5, 10, 0.25, "blue", "circle", 0, 2.0)
    ss.addPlanet(p)

    p = Planet("EARTH", 47.5, 0.5, 0.30, "green", "circle", 0, 2.0)
    ss.addPlanet(p)

    p = Planet("MARS", 50, 45, 0.5, "red", "circle", 0, 1.63)
    ss.addPlanet(p)

    p = Planet("JUPITER", 100, 20, 0.7, "black", "circle", 0, 1)
    ss.addPlanet(p)

    p = Planet("MOON", 30, 10, 0.35, "gray", "circle", 0, 0.8)
    ss.addPlanet(p)

    numTimePeriods = 500
    for aMove in range(numTimePeriods):
        ss.movePlanets()
    
    ss.freeze()