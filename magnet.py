from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random
from colorama import *

class Magnet(gameObj):

    def __init__(self,s):
        self.s = s
        self.img = np.array([[Back.WHITE+'M','M','M'],[Back.WHITE+'M',Back.CYAN+' ',Back.WHITE+'M'],[Back.WHITE+'M',Back.CYAN+' ',Back.WHITE+'M']])
        self.x = self.s.width-7
        self.y = randrange(self.s.gnd-5)
        self.width = 3
        self.height = 3
        self.vel = np.array([-1,0],dtype='float64')
        self.acc = np.array([0,0],dtype='float64')
        self.objType = 'magnet'
    
    def attract(self,m):
        d1 = m.getX()-self.getX()
        m.changeXVel(m.getXVel()-1*d1/5)

        d2 = m.getY()-self.getY()
        m.changeYVel(m.getYVel()-1*d2/5) 