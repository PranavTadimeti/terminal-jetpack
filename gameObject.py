from screen import *
from colorama import *
import numpy as np


class gameObj:

    def __init__(self,index):
        self.img = []
        self.width = 0
        self.height = 0
        self.vel = np.array([0.0, 0.0])
        self.acc = np.array([0.0, 0.0])
        self.index = index

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

        if(new_x > s.wdt-3 or new_x < 0):
            return

        # for i in range(self.height):
        #     for j in range(self.width):
        #         s.display[self.y+i, self.x+j] = " "+Back.BLUE

        self.x = new_x

    def changeY(self, new_y, s):

        if(new_y < 0):
            return

        # for i in range(self.height):
        #     for j in range(self.width):
        #         s.display[self.y+i, self.x+j] = " "+Back.BLUE

        if(new_y > s.gnd-3):
            new_y = s.gnd-3

        self.y = new_y


    def printObject(self,s):

        for i in range(self.height):
            for j in range(self.width):
                s.display[self.y+i, self.x+j] = self.img[i, j]

    def removeObj(self,objList):
        if(self.x == 0):
            objList.remove(self)