from screen import *
from colorama import *
import numpy as np
from gameObject import *

class babyYoda(gameObj):


    def __init__(self,s,index):

        super().__init__()

        self._img = np.array([['<','•','•','>'],['(',' ',' ',')']])

        self._width = 4
        self._height = 2

        self._x = s.getWidth() - 20
        self._y = s.getGnd() - 2

        self._objType = "yoda"
        self._index = index