import numpy as np
from screen import *
from colorama import *


class gameObj:

    def __init__(self):
        self._img = []
        self._width = 0
        self._height = 0
        self._vel = np.array([0.0, 0.0],dtype='float64')
        self._acc = np.array([0.0, 0.0],dtype='float64')
        self._objType = ""
        self._lives = 0
        self._y = 0
        self._x = 0

    def getX(self):
        return self._x 

    def getY(self):
        return self._y

    def getXVel(self):
        return self._vel[0]

    def getYVel(self):
        return self._vel[1]

    def changeXVel(self, newv):
        self._vel[0] = newv

    def changeYVel(self, newv):
        self._vel[1] = newv

    def changeX(self, new_x, s):

        if(new_x >= s.getWidth()-3):
            new_x = s.getWidth()-3
        
        elif(new_x <= 0):
            new_x = 0

        self._x = int(new_x)

    def changeY(self, new_y, s):

        if(new_y < 0):
            new_y = 0

        if(new_y+self._height > s.getGnd()):
            new_y = s.getGnd()-self._height

        self._y = int(new_y)
    
    def getXAcc(self):
        return self._acc[0]
    
    def getYAcc(self):
        return self._acc[1]

    def removeObj(self,objList,ind,s):
        if(self._x == 0):
            objList.remove(self)
            ind -= 1
        
        elif(self._x >= s.getWidth()-3):
            objList.remove(self)
            ind -= 1

        return ind
    
    def getObjType(self):
        return self._objType
    
    def sliceImg(self,i,j):
        return self._img[i,j]
    
    def getHeight(self):
        return self._height
    
    def getWidth(self):
        return self._width
    
    def getObjType(self):
        return self._objType
