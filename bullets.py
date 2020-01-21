from colorama import *
from screen import *
from gameObject import *
import numpy as np


class Bullet(gameObj):

    def __init__(self, s, index):

        super().__init__()
        
        self._img = np.full((1, 3), Back.MAGENTA+"D")
        self._x = 0
        self._y = 0
        self._width = 3
        self._height = 1
        self._vel = np.array([0, 0],dtype='float64')
        self._acc = np.array([0, 0],dtype='float64')
        self._index = index 
        self._objType = "bullet"

    def createBullet(self, x, y): 
        self._x = x+1
        self._y = y
        self._vel[0] = 1

    def checkCollision(self, objList, ind):

        r1 = list(range(self._x-5, self._x+self._width+1))
        r3 = list(range(self._y, self._y+self._height+1))

        s1 = set(r1)
        s3 = set(r3)
        
        for o in objList:
            
            if(o.getObjType() == "beam"):

                r2 = list(range(o.getX()-2, o.getX()+o.getWidth()+1))
                
                r4 = list(range(o.getY(), o.getY()+o.getHeight()+1))

                s2 = set(r2)
                s4 = set(r4)
                

                a1 = s1.intersection(s2)
                a2 = s3.intersection(s4)

                if(len(a1) and len(a2)):

                    objList.remove(o)
                    objList.remove(self)
                    ind -= 2

                    return ind
            
            elif(o.getObjType() == "boss"):

                r2 = list(range(o.getX()-2, o.getX()+o.getWidth()+1))
                        
                r4 = list(range(o.getY(), o.getY()+o.getHeight()+1))

                s2 = set(r2)
                s4 = set(r4)
                        

                a1 = s1.intersection(s2)
                a2 = s3.intersection(s4)

                if(len(a1) and len(a2)):
                    o.setLives(o.getLives()-1)

                    if(o.getLives() == 0):
                        objList.remove(o)
                        
                    objList.remove(self)
                    ind -= 2

                    return ind


        return ind