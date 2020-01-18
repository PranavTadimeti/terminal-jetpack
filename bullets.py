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
        self.vel = np.array([0, 0],dtype='float64')
        self.acc = np.array([0, 0],dtype='float64')
        self.index = index 
        self.objType = "bullet"

    def createBullet(self, x, y):
        self.x = x+1
        self.y = y
        self.vel[0] = 1

    def checkCollision(self, objList, ind):

        r1 = list(range(self.x-10, self.x+self.width+10))
        r3 = list(range(self.y, self.y+self.height+1))
        
        for o in objList:
            
            r2 = list(range(o.getX()-5, o.getX()+o.width+1))
            
            r4 = list(range(o.getY(), o.getY()+o.height+1))

            s1 = set(r1)
            s2 = set(r2)
            s3 = set(r3)
            s4 = set(r4)
            

            a1 = list(s1 & s2)
            a2 = list(s3 & s4)

            # print(a1,a2)

            if(len(a1) and len(a2)):

                if(o.objType == "beam"):
                    objList.remove(o)
                    objList.remove(self)
                    ind -= 2

            return ind