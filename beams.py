from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random
from colorama import *


class Beams(gameObj):

    def __init__(self, s,ind):
        self.s = s
        self.x = s.wdt-10
        self.y = randrange(self.s.gnd-5)
        self.vel = np.array([-1, 0])
        self.acc = np.array([0, 0])
        self.index = ind
    
    def pickType(self):
        i = randrange(3)

        if(i == 0):
            self.img = np.full((1,5),Back.RED+"@")
            self.height = 1
            self.width = 5
        elif(i == 1):
            self.img = np.array([[Back.RED+'@',Back.BLUE+" ",Back.BLUE+" ",Back.BLUE+" ",Back.BLUE+" "],[Back.BLUE+" ",Back.RED+'@',Back.BLUE+" ",Back.BLUE+" ",Back.BLUE+" "],
            [Back.BLUE+" ",Back.BLUE+" ",Back.RED+"@",Back.BLUE+" ",Back.BLUE+" "],[Back.BLUE+" ",Back.BLUE+" ",Back.BLUE+" ",Back.RED+'@',Back.BLUE+" "],
            [Back.BLUE+" ",Back.BLUE+" ",Back.BLUE+" ",Back.BLUE+" ",Back.RED+'@']])
            self.height = 5
            self.width = 5
        else:
            self.img = np.full((5,1),Back.RED+"@")
            self.height = 5
            self.width = 1

