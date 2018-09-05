# projectile.py
# Provides a simple class for modeling the flight of projectiles.

from math import sin, cos, radians

class Projectile():

    """Simulates the flight of simple projectiles near the earth’s
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, angle, velocity, height):
        ''' Creates a projecitle with given angle, initial velocity
        and height'''
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        ''' Updates position of the projectile in given time interval'''
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos
