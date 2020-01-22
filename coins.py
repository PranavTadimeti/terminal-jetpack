from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random


class Coin(gameObj):

    def __init__(self, s,index):

        super().__init__()
        
        self._img = np.full((1, 1), Back.YELLOW+"C")
        self._x = s.getWidth()-7
        self._y = randrange(2,s.getGnd()-5)
        self._width = 1
        self._height = 1
        self._vel = np.array([-1, 0])
        self._acc = np.array([0, 0])
        self._index = index
        self._objType = "coin"  