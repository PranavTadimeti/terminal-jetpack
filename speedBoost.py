from screen import *
from colorama import *
import numpy as np
from gameObject import *
from random import randrange

class Boost(gameObj):

    def __init__(self,s,index):

        super().__init__()
        
        self.img = np.full((1,1),Back.BLUE+"S")
        self.x = s.width-5
        self.y = randrange(s.gnd-3)
        self.vel = np.array([-1,0],dtype='float64')
        self.acc = np.array([0,0],dtype='float64')
        self.height = 1
        self.width = 1
        self.index = index
        self.objType = "boost"
    
