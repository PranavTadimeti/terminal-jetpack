from colorama import *
from screen import *
from gameObject import *
import numpy as np

class bossBullet(gameObj):

    def __init__(self,s,index):

        super().__init__()

        self.img = np.full((3,3),Back.WHITE+" ")
        self.s = s
        self.x = 0
        self.y = 0
        self.width = 3
        self.height = 3
        self.vel = np.array([0, 0],dtype='float64')
        self.acc = np.array([0, 0],dtype='float64')
        self.index = index 
        self.objType = "bossBullet"
    
    def createBullet(self,x,y,bo):
        self.x = x-1
        self.y = y+int(bo.height/2)+2
        self.vel[0] = -3
    
    def checkCollision(self,objList,m,ind):

        r1 = list(range(self.x, self.x+self.width+1))
        r3 = list(range(self.y, self.y+self.height+1))

        s1 = set(r1)
        s3 = set(r3) 

        r2 = list(range(m.getX(),m.getX()+m.width+1))
        r4 = list(range(m.getY(),m.getY()+m.height))

        s2 = set(r2)
        s4 = set(r4)

        a1 = s1.intersection(s2)
        a2 = s3.intersection(s4)

        if(len(a1) and len(a2)):
            m.lives -= 1
            objList.remove(self)
            ind -= 1
            return ind
        
        return ind