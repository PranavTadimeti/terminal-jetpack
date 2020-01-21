from screen import *
from colorama import *
import numpy as np
from gameObject import *
from random import randrange

class Boost(gameObj):

    def __init__(self,s,index):

        super().__init__()
        
        self._img = np.full((1,1),Back.BLUE+"S")
        self._x = s.getWidth()-5
        self._y = randrange(s.getGnd()-3)
        self._vel = np.array([-1,0],dtype='float64')
        self._acc = np.array([0,0],dtype='float64')
        self._height = 1
        self._width = 1
        self._index = index
        self._objType = "boost"
    
