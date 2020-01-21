from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random
from colorama import *

class Magnet(gameObj):

    def __init__(self,s):

        super().__init__()
        
        self._img = np.array([[Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' '],[Back.RED+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' '],[Back.RED+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' '],[Back.RED+' ',Back.CYAN+' ',Back.CYAN+' ',Back.RED+' ']])
        self._x = s.getWidth()-7
        self._y = randrange(s.getGnd()-5)
        self._width = 4
        self._height = 4
        self._vel = np.array([-1,0],dtype='float64')
        self._acc = np.array([0,0],dtype='float64')
        self._objType = 'magnet'
    
    def attract(self,m):
        d1 = m.getX()-self._x
        m.changeXVel(m.getXVel()+(-10*d1))

        d2 = m.getY()-self._y
        m.changeYVel(m.getYVel()+(-10*d2)) 