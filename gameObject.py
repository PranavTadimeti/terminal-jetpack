from screen import *
from colorama import *
import numpy as np


class gameObj:

    def __init__(self):
        self.img = []
        self.width = 0
        self.height = 0
        self.vel = np.array([0.0, 0.0],dtype='float64')
        self.acc = np.array([0.0, 0.0],dtype='float64')
        self.objType = ""
        self.lives = 0

    def getX(self):
        return self.x 

    def getY(self):
        return self.y

    def getXVel(self):
        return self.vel[0]

    def getYVel(self):
        return self.vel[1]

    def changeXVel(self, newv):
        self.vel[0] = newv

    def changeYVel(self, newv):
        self.vel[1] = newv

    def changeX(self, new_x, s):

        if(new_x >= s.width-3):
            new_x = s.width-3
        
        elif(new_x <= 0):
            new_x = 0

        self.x = int(new_x)

    def changeY(self, new_y, s):

        if(new_y < 0):
            new_y = 0

        if(new_y+self.height > s.gnd):
            new_y = s.gnd-self.height

        self.y = int(new_y)

    def printObject(self,s):

        for i in range(self.height):
            for j in range(self.width):
                s.display[self.y+i, self.x+j] = self.img[i, j]

    def removeObj(self,objList,ind,s):
        if(self.x == 0):
            objList.remove(self)
            ind -= 1
        
        elif(self.x >= s.width-3):
            objList.remove(self)
            ind -= 1

        return ind
