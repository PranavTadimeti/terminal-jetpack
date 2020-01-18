from colorama import *
from screen import *
from gameObject import *
import numpy as np


class Bullet(gameObj):

    def __init__(self, s, index):
        self.img = np.full((1, 3), Back.MAGENTA+"D")
        self.s = s
        self.x = 0
        self.y = 0
        self.width = 3
        self.height = 1
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.index = index 
        self.objType = "bullet"

    def createBullet(self, x, y):
        self.x = x+1
        self.y = y
        self.vel[0] = 2

    def checkCollision(self, objList, ind):

        r1 = range(self.x-5, self.x+self.width+7)
        r3 = range(self.y, self.y+self.height+1)
        
        for o in objList:
            
            r2 = range(o.x, o.x+o.width+1)
            
            r4 = range(o.y, o.y+o.height+1)

            s1 = set(r1)
            s2 = set(r3)

            if(s1.intersection(r2) and s2.intersection(r4)):

                if(o.objType == "beam"):
                    objList.remove(o)
                    objList.remove(self)
                    ind -= 2

            return ind
