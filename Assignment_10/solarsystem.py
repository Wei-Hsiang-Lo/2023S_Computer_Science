import turtle

class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0, width/2.0, height/2.0)

    def addSun(self, aSun):
        self.__theSun = aSun

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def movePlanets(self):
        import math
        G = 0.1
        dt = 0.01
        for p in self.__planets:
            name = p.getName()
            if name != 'MOON' and name != 'EARTH':
                newX = p.getX() + p.getVelX() * dt
                newY = p.getY() + p.getVelY() * dt
                p.moveTo(newX, newY)
                
                #calculate the distance between the new position and the sun
                r_x = self.__theSun.getX() - p.getX()
                r_y = self.__theSun.getY() - p.getY()
                r = math.sqrt(r_x**2 + r_y**2)

                #to calculate the new accelerate
                accX = G * self.__theSun.getMass() * r_x / r ** 3
                accY = G * self.__theSun.getMass() * r_y / r ** 3

                #compute and set the new velocity components
                new_velX = p.getVelX() + accX * dt
                new_velY = p.getVelY() + accY * dt
                p.setVelX(new_velX)
                p.setVelY(new_velY)
            elif name == 'EARTH':
                newX = p.getX() + p.getVelX() * dt
                newY = p.getY() + p.getVelY() * dt
                p.moveTo(newX, newY)
                newXofM = self.__planets[4].getX() + self.__planets[4].getVelX() * dt #+ p.getVelX() * dt
                newYofM = self.__planets[4].getY() + self.__planets[4].getVelY() * dt #+ p.getVelY() * dt
                self.__planets[4].moveTo(newXofM, newYofM)

                #calculate the distance between the sun and the earth to obtain the new acc of earth
                r_x = self.__theSun.getX() - p.getX()
                r_y = self.__theSun.getY() - p.getY()
                r = math.sqrt(r_x**2 + r_y**2)
                #calculate the distance between the earth and the moon to obtain the new acc of earth
                r_xOfM = p.getX() - self.__planets[4].getX()
                r_yOfM = p.getY() - self.__planets[4].getY()
                rOfM = math.sqrt(r_xOfM**2 + r_yOfM**2)

                #to calculate the acc of the earth
                accX = G * self.__theSun.getMass() * r_x / r ** 3
                accY = G * self.__theSun.getMass() * r_y / r ** 3
                #to calculate the acc of the moon(this step assume that the earth is motionless)
                accXOfM = G * p.getMass() * r_xOfM / rOfM ** 3
                accYofM = G * p.getMass() * r_yOfM / rOfM ** 3
                #this step improve the acc of the moon
                new_accX = accX + accXOfM
                new_accY = accY + accYofM
                
                #calculate the new velocity of Earth
                new_velX = p.getVelX() + accX * dt
                new_velY = p.getVelY() + accY * dt
                p.setVelX(new_velX)
                p.setVelY(new_velY)
                #calculate the new velocity of moon
                new_velXofM = self.__planets[4].getVelX() + new_accX * dt
                new_velYofM = self.__planets[4].getVelY() + new_accY * dt
                self.__planets[4].setVelX(new_velXofM)
                self.__planets[4].setVelY(new_velYofM)
                
    def freeze(self):
        self.__ssScreen.exitonclick()