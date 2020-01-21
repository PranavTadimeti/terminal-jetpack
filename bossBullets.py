from colorama import *
from screen import *
from gameObject import *
import numpy as np

class bossBullet(gameObj):

    def __init__(self,s,index):

        super().__init__()

        self._img = np.full((2,3),Back.WHITE+" ")
        self._s = s
        self._x = 0
        self._y = 0
        self._width = 3
        self._height = 2
        self._vel = np.array([0, 0],dtype='float64')
        self._acc = np.array([0, 0],dtype='float64')
        self._index = index 
        self._objType = "bossBullet"
    
    def createBullet(self,x,y,m):
        self._x = x-1
        self._y = m.getY()
        self._vel[0] = -3
    
    def checkCollision(self,objList,m,ind):

        r1 = list(range(self._x, self._x+self._width+1))
        r3 = list(range(self._y, self._y+self._height+1))

        s1 = set(r1)
        s3 = set(r3) 

        r2 = list(range(m.getX(),m.getX()+m.getWidth()+1))
        r4 = list(range(m.getY(),m.getY()+m.getHeight()))

        s2 = set(r2)
        s4 = set(r4)

        a1 = s1.intersection(s2)
        a2 = s3.intersection(s4)

        if(len(a1) and len(a2)):
            m.setLives(m.getLives()-1)
            objList.remove(self)
            ind -= 1
            return ind
        
        return ind