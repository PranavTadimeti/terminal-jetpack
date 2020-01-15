from screen import *
from gameObject import *
import numpy as np
from random import randint, randrange, random


class Coin(gameObj):

    def __init__(self, s):
        self.img = np.full((4, 5), Back.YELLOW+"C")
        self.s = s
        self.x = s.wdt-10
        self.y = randrange(self.s.gnd)
        self.width = 5
        self.height = 4
        self.vel = np.array([-1, 0])
        self.acc = np.array([0, 0])

    def printCoin(self):

        for i in range(self.height):
            for j in range(self.width):
                self.s.display[self.y+i, self.x+j] = self.img[i,j]


    def checkEdge(self):
        if(self.x == 0):
            self.s.display[self.y:self.y+self.height, self.x:self.x+self.width] = " "+Back.BLUE
