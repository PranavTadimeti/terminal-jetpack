from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random
from colorama import *

class Magnet(gameObj):

    def __init__(self,s):

        super().__init__()
        
        self.s = s
        self.img = np.array([[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' '],[Back.RED+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' '],[Back.RED+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' '],[Back.RED+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' ']])
        self.x = self.s.width-7
        self.y = randrange(self.s.gnd-5)
        self.width = 4
        self.height = 4
        self.vel = np.array([-1,0],dtype='float64')
        self.acc = np.array([0,0],dtype='float64')
        self.objType = 'magnet'
    
    def attract(self,m):
        d1 = m.getX()-self.getX()
        m.changeXVel(m.getXVel()+(-10*d1))

        d2 = m.getY()-self.getY()
        m.changeYVel(m.getYVel()+(-10*d2)) 