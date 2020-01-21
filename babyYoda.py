from screen import *
from colorama import *
import numpy as np
from gameObject import *

class babyYoda(gameObj):


    def __init__(self,s,index):

        super().__init__()

        self.img = np.array([['<','•','•','>'],['(',' ',' ',')']])

        self.width = 4
        self.height = 2

        self.x = s.width - 20
        self.y = s.gnd - 2

        self.objType = "yoda"
        self.index = index