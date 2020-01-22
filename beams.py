from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random
from colorama import *


class Beams(gameObj):

    def __init__(self, s,ind):

        super().__init__()
        
        self._x = s.getWidth()-7
        self._y = randrange(2,s.getGnd()-5)
        self._vel = np.array([-1, 0])
        self._acc = np.array([0, 0])
        self._index = ind
        self._objType = "beam"
     
    def pickType(self):
        i = randrange(3)

        if(i == 0):
            self._img = np.full((1,7),Back.RED+"@")
            self._height = 1
            self._width = 7
        elif(i == 1):
            self._img = np.array([[Back.RED+'@',Back.CYAN+" ",Back.CYAN+" ",Back.CYAN+" ",Back.CYAN+" "],[Back.CYAN+" ",Back.RED+'@',Back.CYAN+" ",Back.CYAN+" ",Back.CYAN+" "],
            [Back.CYAN+" ",Back.CYAN+" ",Back.RED+"@",Back.CYAN+" ",Back.CYAN+" "],[Back.CYAN+" ",Back.CYAN+" ",Back.CYAN+" ",Back.RED+'@',Back.CYAN+" "],
            [Back.CYAN+" ",Back.CYAN+" ",Back.CYAN+" ",Back.CYAN+" ",Back.RED+'@']])
            self._height = 5
            self._width = 5
        else:
            self._img = np.full((5,1),Back.RED+"@")
            self._height = 5
            self._width = 1

