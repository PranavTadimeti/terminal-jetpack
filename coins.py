from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random


class Coin(gameObj):

    def __init__(self, s,index):
        self.img = np.full((1, 1), Back.YELLOW+"C")
        self.s = s
        self.x = s.wdt-7
        self.y = randrange(self.s.gnd-5)
        self.width = 1
        self.height = 1
        self.vel = np.array([-1, 0])
        self.acc = np.array([0, 0])
        self.index = index
        self.objType = "coin" 